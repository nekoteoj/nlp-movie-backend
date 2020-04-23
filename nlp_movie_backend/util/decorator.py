import copy


def singleton(factory):
    resource = None

    def get_resource():
        nonlocal resource
        if resource is None:
            resource = factory()
        return resource

    return get_resource


def deepcopy(factory):
    def get_resource():
        return copy.deepcopy(factory())

    return get_resource
