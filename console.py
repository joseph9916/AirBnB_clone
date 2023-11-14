#!/usr/bin/python3
"""
entry point of the command interpreter
"""


import cmd
import re
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.state import State
from models.review import Review
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
        elif (args[0] == "BaseModel" or args[0] == "User" or
                args[0] == "Place" or args[0] == "City" or
                args[0] == "Amenity" or args[0] == "Review"
                or args[0] == "State"):
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
        elif (args[0] == "BaseModel" or args[0] == "User" or
                args[0] == "Place" or args[0] == "City" or
                args[0] == "Amenity" or args[0] == "Review"
                or args[0] == "State"):
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
        if (arg is None or arg == "" or arg == "BaseModel"
               or arg == "User" or arg == "Place" or arg == "City" or
               arg == "Amenity" or arg == "Review" or arg == "State"):
            all_objs = storage.all()
            list_objs = []
            for key in all_objs.keys():
                if arg is None:
                    list_objs.append(all_objs[key].__str__())
                else:
                    if arg in key:
                        list_objs.append(all_objs[key].__str__())
            print(list_objs)
        else:
            print("** class doesn't exist **")

    def do_User(self, arg):
        """Handles all commands for Users"""
        if "all" in arg:
            self.do_all("User")
        args = "User {}"re.findall('"([^"]*)"', arg)[0]
        elif "show" in arg:
            self.do_show(arg)
        elif "update" in arg:
            self.do_update(args)
        elif "destroy" in arg:
            self.do_destroy(args)

    def do_State(self, arg):
        """Shows all instances of States Class"""
        if "all" in arg:
            self.do_all("State")
        args = "State {}"re.findall('"([^"]*)"', arg)[0]
        elif "show" in arg:
            self.do_show(args)
        elif "update" in arg:
            self.do_update(args)
        elif "destroy" in arg:
            self.do_destroy(args)

    def do_Place(self, arg):
        """Shows all instances for Places Class"""
        if "all" in arg:
            self.do_all("Place")
        args = "Place {}"re.findall('"([^"]*)"', arg)[0]
        elif "show" in arg:
            self.do_show(args)
        elif "update" in arg:
            self.do_update(args)
        elif "destroy" in arg:
            self.do_destroy(args)

    def do_City(self, arg):
        """Shows all instances for City Class"""
        if "all" in arg:
            self.do_all("City")
        args = "City {}"re.findall('"([^"]*)"', arg)[0]
        elif "show" in arg:
            self.do_show(args)
        elif "update" in arg:
            self.do_update(args)
        elif "destroy" in arg:
            self.do_destroy(args)

    def do_Amenity(self, arg):
        """Shows all instances for Amenity Class"""
        if "all" in arg:
            self.do_all("Amenity")
        args = "Amenity {}"re.findall('"([^"]*)"', arg)[0]
        elif "show" in arg:
            self.do_show(args)
        elif "update" in arg:
            self.do_update(args)
        elif "destroy" in arg:
            self.do_destroy(arg)

    def do_Review(self, arg):
        """Shows all instances for Review Class"""
        if "all" in arg:
            self.do_all("Review")
        args = "Amenity {}"re.findall('"([^"]*)"', arg)[0]
        elif "show" in arg:
            self.do_show("City")
        elif "update" in arg:
            self.do_update(args)
        elif "destroy" in arg:
            self.do_destroy(args)

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
        elif (args[0] == "BaseModel" or args[0] == "User" or
                args[0] == "Place" or args[0] == "City" or
                args[0] == "Amenity" or args[0] == "Review"
                or args[0] == "State"):
            key = "{}.{}".format(args[0], args[1])
            with open("file.json", "r+", encoding="utf-8") as f:
                json_string = f.read()
                all_objs_dict = json.loads(json_string)
                if key in all_objs_dict.keys():
                    print("Here")
                    obj_dict = all_objs_dict[key]
                    if len(args) >= 3:
                        if len(args) < 4:
                            print("** value missing **")
                        else:
                            print("Here")
                            obj_dict[args[2]] = args[3]
                            if args[0] == "BaseModel":
                                BaseModel(obj_dict)
                            if args[0] == "User":
                                print("Here")
                                setattr(User, args[2], args[3])
                            if args[0] == "Place":
                                Place(obj_dict)
                            if args[0] == "City":
                                City(obj_dict)
                            if args[0] == "Amenity":
                                Amenity(obj_dict)
                            if args[0] == "Review":
                                Review(obj_dict)
                            if args[0] == "State":
                                State(obj_dict)
                            storage.save()
                            storage.reload()
                    else:
                        print("** attribute name missing **")
                else:
                    print("** no instance found **")
        else:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
