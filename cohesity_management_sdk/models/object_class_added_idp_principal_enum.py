# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.

class ObjectClassAddedIdpPrincipalEnum(object):

    """Implementation of the 'ObjectClass_AddedIdpPrincipal' enum.

    Specifies the type of the referenced Idp principal.
    If 'kGroup', the referenced Idp principal is a group.
    If 'kUser', the referenced Idp principal is a user.
    'kUser' specifies a user object class.
    'kGroup' specifies a group object class.
    'kComputer' specifies a computer object class.
    'kWellKnownPrincipal' specifies a well known principal.

    Attributes:
        KUSER: TODO: type description here.
        KGROUP: TODO: type description here.
        KCOMPUTER: TODO: type description here.
        KWELLKNOWNPRINCIPAL: TODO: type description here.

    """

    KUSER = 'kUser'

    KGROUP = 'kGroup'

    KCOMPUTER = 'kComputer'

    KWELLKNOWNPRINCIPAL = 'kWellKnownPrincipal'

