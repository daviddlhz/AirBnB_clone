#!/usr/bin/python3
"""console v0.1
"""

import cmd
import json
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """command interpreter of AirBnB project
    """
    classes = {"BaseModel"}
    prompt = '(hbnb) '

    def do_EOF(self, line):
        """Ctrl D - the program will exit cleanly
        """
        return True

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    def emptyline(self):
        """Called when an empty line is entered in response to the prompt
        """
        pass

    def do_create(self, line):
        """Create a new instance of BaseModel, saves it
        (to the JSON file) and prints the id
        """
        args = line.split(' ')
        if len(args) < 1:
            print("** class name missing **")
        elif len(args) >= 1:
            if args[0] not in HBNBCommand.classes:
                print("** class doesn't exist **")
            else:
                n_instance = eval(str(args[0]) + '()')
                print(n_instance)
                n_instance.save()

    def do_show(self, line):
        """ Prints the string representation of an instance
        based on the class name and id
        """
        args = line.split(' ')
        if len(args) == 0:
            print('** class name missing **')
            return
        elif args[0] not in HBNBCommand.classes:
            print('** class doesn\'t exist **')
            return
        elif len(args) == 1:
            print('** instance id missing **')
            return
        else:
            all_objs = storage.all()
            k_find = args[0] + '.' + args[1]
            if k_find in all_objs:
                print(all_objs[k_find])
                return
            else:
                print('** no instance found **')
                pass

    def do_destroy(self, line):
        """Deletes an instance based on the class name
        and id (save the change into the JSON file).
        """
        args = line.split(' ')
        if len(args) == 0:
            print("** class name missing **")
            return
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        else:
            all_objs = storage.all()
            k_find = args[0] + '.' + args[1]
            if k_find in all_objs:
                del all_objs[k_find]
                storage.save()
                return
            else:
                print('** no instance found **')
                pass

    def do_all(self, line):
        """Prints all string representation of all instances
        based or not on the class name.
        """
        args = line.split(' ')
        if len(args) == 0:
            all_objs = storage.all()
            new_list = []
            for obj_id in all_objs.keys():
                obj = all_objs[obj_id]
                new_list.append("{}".format(obj))
            print(new_list)
        elif len(args) == 1:
            if args[0] in HBNBCommand.classes:
                for keys in storage.all().values():
                    if args[0] in HBNBCommand.classes:
                        new_list.append(str(keys))
                print('{}'.format(new_list))
            else:
                print('** class doesn\'t exist **')

    def do_update(self, line):
        """ Updates an instance based on the class name
        and id by adding or updating attribute
        (save the change into the JSON file)
        """
        args = line.split(' ')
        obj = storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif len(args) == 1:
            if args[0] not in HBNBCommand.classes:
                print("** class doesn't exist **")
            else:
                print("** instance id missing **")
        elif len(args) == 2:
            k_find = args[0] + '.' + args[1]
            if k_find not in obj:
                print('** no instance found **')
            else:
                print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        elif len(args) >= 4:
            objx = obj[args[0] + '.' + args[1]]
            if args[2] in objx.__dict__:
                objx.__dict__[args[2]] = eval(args[3])
            else:
                objx.__dict__[args[2]] = eval(args[3])
        storage.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
