def to_decimal(latitude, longitude):

    def convert(coordinate, pos_dir, neg_dir):
        degrees, minutes, seconds, direction = coordinate

        # Make direction case-insensitive
        direction = direction.upper() # This is to make sure that direction input are case sensitive.

        if not 0 <= minutes < 60 or not 0 <= seconds < 60:
            raise ValueError("minutes and seconds must be in the range [0, 60)")

        value = degrees + minutes / 60 + seconds / 3600

        return -value if direction == neg_dir else value

    lat_decimal = convert(latitude, "N", "S")
    lon_decimal = convert(longitude, "E", "W")

    return lat_decimal, lon_decimal


def to_degree(lat_value, lon_value):

    def convert(value, pos_dir, neg_dir):

        # Determine direction based on sign
        direction = neg_dir if value < 0 else pos_dir

        absolute_value = abs(value)

        degrees = int(absolute_value)
        minutes_value = (absolute_value - degrees) * 60
        minutes = int(minutes_value)
        seconds = (minutes_value - minutes) * 60

        if seconds >= 60:
            seconds = 0.00
            minutes += 1

        if minutes >= 60:
            minutes = 0
            degrees += 1

        return degrees, minutes, seconds, direction

    lat_dms = convert(lat_value, "N", "S")
    lon_dms = convert(lon_value, "E", "W")

    return lat_dms, lon_dms
