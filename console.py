#!/usr/bin/python3
"""
entry point of the command interpreter
"""


import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
import json
import os


class HBNBCommand(cmd.Cmd):
    """entry point of the command interpreter"""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit the console"""
        return True

    # aliasing
    do_EOF = do_quit

    def emptyline(self):
        """What to do in a emptyline"""
        pass

    def do_create(self, arg):
        """create a basemodel"""
        if arg is None or arg == "":
            print("** class name missing **")
        elif arg == "BaseModel":
            new = BaseModel()
            new.save()
            print(new.id)
        elif arg == "User":
            new = User()
            new.save()
            print(new.id)
        elif arg == "State":
            new = State()
            new.save()
            print(new.id)
        elif arg == "City":
            new = City()
            new.save()
            print(new.id)
        elif arg == "Amenity":
            new = Amenity()
            new.save()
            print(new.id)
        elif arg == "Place":
            new = City()
            new.save()
            print(new.id)
        elif arg == "Review":
            new = Review()
            new.save()
            print(new.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """show a basemodel based on its id"""
        args = arg.split()
        if arg is None or arg == "":
            print("** class name missing **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif (args[0] == "BaseModel" or arg[0] == "User" or
                args[0] == "Place" or args[0] == "City" or
                args[0] == "Amenity" or args[0] == "Review"):
            if os.path.isfile("file.json"):
                all_objs = storage.all()
                # with open("file.json", "r", encoding="utf-8") as f:
                # obj_dicts = json.load(f)
                key = "{}.{}".format(args[0], args[1])
                if key in all_objs.keys():
                    print(all_objs[key])
                else:
                    print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """destroy a basemodel based on its id"""
        args = arg.split()
        if arg is None or arg == "":
            print("** class name missing **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif (args[0] == "BaseModel" or arg[0] == "User" or
                args[0] == "Place" or args[0] == "City" or
                args[0] == "Amenity" or args[0] == "Review"):
            if os.path.isfile("file.json"):
                all_objs = storage.all()
                key = "{}.{}".format(args[0], args[1])
                if key in all_objs.keys():
                    all_objs.pop(key)
                    storage.save()
                else:
                    print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """Prints all string representation of all instances based or
        not on the class name"""
        if arg is None or arg == "" or arg == "BaseModel":
            all_objs = storage.all()
            list_objs = []
            for key in all_objs.keys():
                list_objs.append(all_objs[key].__str__())
            print(list_objs)
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding
        or updating attribute
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        all_objs = storage.all()
        args = arg.split()
        if arg is None or arg == "":
            print("** class name missing **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif (args[0] == "BaseModel" or arg[0] == "User" or
                args[0] == "Place" or args[0] == "City" or
                args[0] == "Amenity" or args[0] == "Review"):
            key = "{}.{}".format(args[0], args[1])
            if key in all_objs.keys():
                obj = all_objs[key]
                if len(args) >= 3:
                    if len(args) < 4:
                        print("** value missing **")
                    else:
                        obj[args[2]] = args[3]
                else:
                    print("** attribute name missing **")
            else:
                print("** no instance found **")
        else:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
