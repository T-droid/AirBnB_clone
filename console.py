#!/usr/bin/python3
import cmd
from models.base_model import BaseModel

"""script to impliment the console"""

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    """class to create the commandline using cmd"""

    def do_quit(self, commands):
        """Quit command to exit the program"""
        return True

    def do_EOF(self):
        """End of file"""
        return

    def do_create(self, cls_name):
        """Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id"""
        if not cls_name:
            print("** class name missing **")

        elif cls_name not in globals() or not isinstance(globals()[cls_name], type):
            print("** class doesn't exist **")

        else:
            new = BaseModel()
            new.save()
            print("{}".format(new.id))

    @staticmethod
    def find_with_id(cls_name, user_id):
        """finds an instance based on the id"""
        for key, value in globals().items():
            if isinstance(value, type) and issubclass(value, BaseModel):
                if key != cls_name:
                    continue
                instance_var_name = f"{key}.{user_id}"
                if instance_var_name in globals():
                    return globals()[instance_var_name]
        return None

    def do_show(self, args):
        """Prints the string representation of an instance based on the class name and id"""
        args = args.split()
        if not args:
            print("** class name missing **")
        elif len(args) < 2:
            print("** instance id missing **")

        else:
            cls_name, user_id = args[0], args[1]
            if cls_name not in globals() or not isinstance(globals()[cls_name], type):
                print("** class doesn't exist **")

            else:
                value = __class__.find_with_id(cls_name, user_id)
                if value is None:
                    print("** no instance found **")
                else:
                    print(value)


    def do_destroy(self, args):
        """Deletes an instance based on the class name and id (save the change into the JSON file)"""
        args = args.split()

        if not args:
            print("** class name missing **")

        elif len(args) < 2:
            print("** instance id missing **")

        else:
            cls_name, user_id = args[0], args[1]
            if cls_name not in globals() or not isinstance(globals()[cls_name], type):
                print("** class doesn't exist **")

            elif user_id not in globals() or not isinstance(globals()[user_id], type):
                print("** no instance found **")

            else:
                value = __class__.find_with_id(cls_name, user_id)
                del value

    def do_all(self, cls_name):
        """Prints all string representation of all instances based or not on the class name."""
        all_instances = [obj for obj in globals().values() if isinstance(obj, type) and issubclass(obj, BaseModel)]
        if cls_name:
            all_instances = [obj for obj in all_instances if obj.__name__ == cls_name]
            print(all_instances)

        else:
            print("No instance found")

    def do_update(self, args):
        """ Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file)."""
        args = args.split()

        if not args:
            print("** class name missing **")

        elif len(args) < 2:
            print("** instance id missing **")

        elif len(args) < 3:
            print("** attribute name missing **")

        elif len(args) < 4:
            print("** value missing **")

        else:
            cls_name, id, attribute_name, attribute_value = args[0], args[1], args[2], args[3]
            print(f"update {cls_name} with id {id} {attribute_name} of value {attribute_value}")

if __name__ == '__main__':
    HBNBCommand().cmdloop()