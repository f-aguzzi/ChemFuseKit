'''__init__.py file for the library'''
from beartype import BeartypeConf
from beartype.claw import beartype_this_package
beartype_this_package(conf=BeartypeConf(violation_type=TypeError))
