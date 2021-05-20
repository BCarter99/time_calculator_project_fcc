def add_time(start, duration, day_of_week=False):

    days_of_the_week_index = {'Monday': 0, 'Tuesday': 1, 'Wednesday': 2, 'Thursday': 3, 'Friday': 4, 'Saturday': 5, 'Sunday': 6}

    days_of_the_week_array = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    # finds the starting hour and minute positions
    [start_time, am_pm] = start.split(' ')
    [starting_hour, starting_minutes] = [int(i) for i in start_time.split(':')]

    # finds the duration hour and minute positions
    [duration_hour, duration_minutes] = [int(i) for i in duration.split(':')]

    am_pm_flip = {'AM':'PM', 'PM':'AM'}

    days_passed = duration_hour // 24

    # calculates the resulting minutes, keeping track of whether an extra hour has passed
    end_minutes = starting_minutes + duration_minutes
    if end_minutes >= 60:
        starting_hour += 1
        end_minutes = end_minutes % 60

    # determines the number used to decide if the AM/PM needs to switch
    amount_of_am_pm_flips = (starting_hour + duration_hour) // 12

    end_hours = (starting_hour + duration_hour) % 12

    # adds a 0 to the front of any minutes less than 9, in order to format correctly
    end_minutes = end_minutes if end_minutes > 9 else '0' + str(end_minutes)
    end_hours = 12 if end_hours == 0 else end_hours
    if (am_pm == 'PM' and starting_hour + (duration_hour % 12) >= 12):
        days_passed += 1

    am_pm = am_pm_flip[am_pm] if amount_of_am_pm_flips % 2 == 1 else am_pm

    resulting_time = f'{end_hours}:{end_minutes} {am_pm}'
    if day_of_week:
        day_of_week = day_of_week.capitalize()
        index = int((days_of_the_week_index[day_of_week]) + days_passed) % 7
        end_day = days_of_the_week_array[index]
        resulting_time += f', {end_day}'

    if days_passed == 1:
        return resulting_time + f' (next day)'
    elif days_passed > 1:
        return resulting_time + f' ({days_passed} days later)'


    return resulting_time