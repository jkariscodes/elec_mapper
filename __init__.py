# -*- coding: utf-8 -*-
"""
/***************************************************************************
 ElecMapper
                                 A QGIS plugin
 This plugin creates and digitizes pylon location as points and grid connectors as lines layers in QGIS.
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2022-09-26
        copyright            : (C) 2022 by Joseph Kariuki
        email                : joehene@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load ElecMapper class from file ElecMapper.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .elec_mapper import ElecMapper
    return ElecMapper(iface)
