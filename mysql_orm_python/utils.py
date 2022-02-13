from .model import Model

def get_all_subclasses(parent_class):
    """Return all subclasses of a python class.

    Args:
        parent_class (Type): python class

    Returns:
        list: list of python subclasses
    """
    sub_classes = []
    # if super-class, get a list of sub-classes.
    # Otherwise use component_class to create objects.
    try:
        derived_classes = parent_class.__subclasses__()
        if not derived_classes:
            sub_classes.append(parent_class)
        else:
            sub_classes.extend(derived_classes)
    except AttributeError:
        sub_classes.append(parent_class)
    return sub_classes

def get_all_models():
    return get_all_subclasses(Model)

def duplicates(l): 
    return [el for ind, el in enumerate(l) if el in l[:ind]]