import runtime_configuration
import os


def get_resource_directory():
    application_path = runtime_configuration.get_application_directory()
    return os.path.join(application_path, "res")


def load_resource(image_name, directory=None):
    if directory:
        return os.path.join(get_resource_directory(), directory, image_name)
    else:
        return os.path.join(get_resource_directory(), image_name)
