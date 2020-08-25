raw_minutes = int(input('Hur många minuter? '))

minutes = raw_minutes % 60
hours = (raw_minutes / 60) - (minutes / 60)

hours, minutes = int(hours), int(minutes)

hour_form = 'timmar'
minute_form = 'minuter'

if hours == 1:
	hour_form = 'timme'

if minutes == 1:
	minute_form = 'minut'

message = f'Det är {hours} {hour_form}'
if minutes:
	message += f' och {minutes} {minute_form}'
message += '.'

print(message)
