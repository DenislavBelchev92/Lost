#!/usr/bin/env python

from apps.beacons.models import Beacon

# Utilities - start {
index_context = {
    'beacon_types': Beacon.beacon_choices,
}
