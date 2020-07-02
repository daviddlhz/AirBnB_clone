#!/usr/bin/python3
"""console v0.1
"""

import cmd
import json
import shlex
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """command interpreter of AirBnB project
    """
    classes = {'BaseModel': BaseModel, 'User': User,
               'Place': Place, 'State': State,
               'City': City, 'Amenity': Amenity,
               'Review': Review}

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
            if args[0] not in self.classes:
                print("** class doesn't exist **")
            else:
                n_instance = eval(str(args[0]) + '()')
                print(n_instance.id)
                n_instance.save()

    def do_show(self, line):
        """ Prints the string representation of an instance
        based on the class name and id
        """
        args = line.split(' ')
        if len(args) == 0:
            print('** class name missing **')
            return
        elif args[0] not in self.classes:
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
        elif args[0] not in self.classes:
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
        instance = storage.all()
        new_list = []
        if len(line) == 0:
            for value in instance.values():
                new_list.append(value.__str__())
            print(new_list)
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        else:
            for value in instance.values():
                if args[0] == value.__class__.__name__:
                    new_list.append(value.__str__())
            print(new_list)
            return

    def do_update(self, line):
        """ Updates an instance based on the class name
        and id by adding or updating attribute
        (save the change into the JSON file)
        """
        args = line.split(' ')
        objects = storage.all()

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            key_find = args[0] + '.' + args[1]
            obj = objects.get(key_find, None)
            if not obj:
                print("** no instance found **")
                return
            setattr(obj, args[2], args[3].lstrip('"').rstrip('"'))
            storage.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
