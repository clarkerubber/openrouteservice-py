# Copyright 2014 Google Inc. All rights reserved.
#
# Modifications Copyright (C) 2018 HeiGIT, University of Heidelberg.
#
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not
# use this file except in compliance with the License. You may obtain a copy of
# the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations under
# the License.
#

"""Performs requests to the ORS directions API."""

import json

from openrouteservice import convert, validator

def directions(client,
               coordinates,
               profile='driving-car',
               format_out=None,
               preference=None,
               units=None,
               language=None,
               geometry=None,
               geometry_format=None,
               geometry_simplify=None,
               instructions=None,
               instructions_format=None,
               roundabout_exits=None,
               attributes=None,
               # maneuvers=None,
               radiuses=None,
               bearings=None,
               continue_straight=None,
               elevation=None,
               extra_info=None,
               optimized='true',
               options=None,
               dry_run=None):
    """Get directions between an origin point and a destination point.

    For more information, visit https://go.openrouteservice.org/documentation/.

    :param coordinates: The coordinates tuple the route should be calculated
        from. In order of visit.
    :type origin: list or tuple of coordinate lists or tuples

    :param profile: Specifies the mode of transport to use when calculating
        directions. One of ["driving-car", "driving-hgv", "foot-walking",
        "foot-hiking", "cycling-regular", "cycling-road",requests_kwargs
        "cycling-safe", "cycling-mountain", "cycling-tour",
        "cycling-electric",]. Default "driving-car".
    :type mode: string

    :param preference: Specifies the routing preference. One of ["fastest, "shortest",
        "recommended"]. Default "fastest".
    :type preference: string

    :param units: Specifies the distance unit. One of ["m", "km", "mi"]. Default "m".
    :type units: string

    :param language: Language for routing instructions. One of ["en", "de", "cn",
        "es", "ru", "dk", "fr", "it", "nl", "br", "se", "tr", "gr"]. Default "en".
    :type language: string

    :param language: The language in which to return results.
    :type language: string

    :param geometry: Specifies whether geometry should be returned. "true" or "false".
        Default "true".
    :type geometry: string

    :param geometry_format: Specifies which geometry format should be returned.
        One of ["encodedpolyline", "geojson", "polyline"]. Default: "encodedpolyline".
    :type geometry_format: string

    :param geometry_simplify: Specifies whether to simplify the geometry.
        "true" or "false". Default "false".
    :type geometry_simplify: boolean as string

    :param instructions: Specifies whether to return turn-by-turn instructions.
        "true" or "false". Default "true".
    :type instructions: string

    :param instructions_format: Specifies the the output format for instructions.
        One of ["text", "html"]. Default "text".
    :type instructions_format: string

    :param roundabout_exits: Provides bearings of the entrance and all passed
        roundabout exits. Adds the 'exit_bearings' array to the 'step' object
        in the response. "true" or "false". Default "false".
    :type roundabout_exits: string

    :param attributes: Returns route attributes on ["avgspeed", "detourfactor", "percentage"].
        Must be a list of strings. Default None.
    :type attributes: list or tuple of strings

    :param radiuses: A list of maximum distances (measured in
        meters) that limit the search of nearby road segments to every given waypoint.
        The values must be greater than 0, the value of -1 specifies no limit in
        the search. The number of radiuses must correspond to the number of waypoints.
        Default None.
    :type radiuses: list or tuple

    :param bearings: Specifies a list of pairs (bearings and
        deviations) to filter the segments of the road network a waypoint can
        snap to. For example bearings=[[45,10],[120,20]]. Each pair is a
        comma-separated list that can consist of one or two float values, where
        the first value is the bearing and the second one is the allowed deviation
        from the bearing. The bearing can take values between 0 and 360 clockwise
        from true north. If the deviation is not set, then the default value of
        100 degrees is used. The number of pairs must correspond to the number
        of waypoints. Setting optimized=false is mandatory for this feature to
        work for all profiles. The number of bearings corresponds to the length
        of waypoints-1 or waypoints. If the bearing information for the last waypoint
        is given, then this will control the sector from which the destination
        waypoint may be reached.
    :type bearings: list or tuple or lists or tuples

    :param continue_straight: Forces the route to keep going straight at waypoints
        restricting u-turns even if u-turns would be faster. This setting
        will work for all profiles except for driving-*. In this case you will
        have to set optimized=false for it to work. True or False. Default False.
    :type continue_straight: boolean

    :param elevation: Specifies whether to return elevation values for points.
        "true" or "false". Default "false".
    :type elevation: boolean as string

    :param extra_info: Returns additional information on ["steepness", "suitability",
        "surface", "waycategory", "waytype", "tollways", "traildifficulty"].
        Must be a list of strings. Default None.
    :type extra_info: list or tuple of strings

    :param optimized: If set True, uses Contraction Hierarchies. "true" or "false".
        Default "true".
    :type optimized: boolean as string

    :param options: Refer to https://go.openrouteservice.org/documentation for
        detailed documentation. Construct your own dict() following the example
        of the minified options object. Will be converted to json automatically.
    :type options: dict

    :raises ValueError: When parameter has wrong value.
    :raises TypeError: When parameter is of wrong type.

    :rtype: call to Client.request()
    """

    params = {
        "coordinates": coordinates
        }

    if profile:
        # NOTE(broady): the mode parameter is not validated by the Maps API
        # server. Check here to prevent silent failures.
        params["profile"] = profile

    if format_out:
        params["format"] = format_out

    if preference:
        params["preference"] = preference

    if units:
        params["units"] = units

    if language:
        params["language"] = language

    if geometry:
        params["geometry"] = geometry

    if geometry_format:
        params["geometry_format"] = geometry_format

    if geometry_simplify:
        if extra_info:
            params["geometry_simplify"] = 'false'
        else:
            params["geometry_simplify"] = geometry_simplify

    if instructions:
        params["instructions"] = instructions

    if instructions_format:
        params["instructions_format"] = instructions_format

    if roundabout_exits:
        params["roundabout_exits"] = roundabout_exits

    if attributes:
        params["attributes"] = attributes

    if radiuses:
        params["radiuses"] = radiuses

    if bearings:
        params["bearings"] = bearings

    if continue_straight:
        params["continue_straight"] = continue_straight

    if elevation:
        params["elevation"] = elevation

    if extra_info:
        params['extra_info'] = extra_info

    if optimized:
        params["optimized"] = optimized

    if options:
        params['options'] = options

    # Check all passed arguments
    convert._is_valid_args(params, "directions")

    # Format all passed arguments
    params["coordinates"] = convert._build_coords(coordinates)

    if attributes:
        params["attributes"] = convert._pipe_list(attributes)

    if radiuses:
        params["radiuses"] = convert._pipe_list(radiuses)

    if bearings:
        params["bearings"] = convert._pipe_list([convert._comma_list(pair) for pair in bearings])

    if continue_straight:
        params["continue_straight"] = continue_straight

    if extra_info:
        params["extra_info"] = convert._pipe_list(extra_info)

    if options:
        params['options'] = json.dumps(options)

    return client.request("/directions", params, dry_run=dry_run)
