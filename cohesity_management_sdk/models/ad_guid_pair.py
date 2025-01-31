# -*- coding: utf-8 -*-
# Copyright 2021 Cohesity Inc.


class AdGuidPair(object):

    """Implementation of the 'AdGuidPair' model.

    AdGuidPair is the AD object guid string pair.

    Attributes:
        destination (string): Specifies the destination guid in production AD
            object corresponding to source. If empty, it assumed to be
            'source' guid.
        source (string): Specifies the source guid string of an AD object in
            mounted AD snapshot. This cannot be empty.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "destination":'destination',
        "source":'source'
    }

    def __init__(self,
                 destination=None,
                 source=None):
        """Constructor for the AdGuidPair class"""

        # Initialize members of the class
        self.destination = destination
        self.source = source


    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        destination = dictionary.get('destination')
        source = dictionary.get('source')

        # Return an object of this model
        return cls(destination,
                   source)


