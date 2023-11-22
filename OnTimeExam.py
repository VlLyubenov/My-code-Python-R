exam_hour = int(input())
exam_minute = int(input())
arrival_hour = int(input())
arrival_minute = int(input())

def time_in_minutes(hour, minutes):
    return hour * 60 + minutes

exam_time = time_in_minutes(exam_hour, exam_minute)
arrival_time = time_in_minutes(arrival_hour, arrival_minute)

output1 = ""
if exam_time - 30 <= arrival_time <= exam_time:
    output1 = "On time"
elif arrival_time < exam_time - 30:
    output1 = "Early"
elif arrival_time > exam_time:
    output1 = "Late"

output2 = ""
if exam_time != arrival_time:

    if arrival_time < exam_time and arrival_time > exam_time - 60:
        output2 = f"{exam_time - arrival_time} minutes before the start"
    elif arrival_time <= exam_time - 60:
        hours = (exam_time - arrival_time) // 60
        minutes = (exam_time - arrival_time) % 60
        output2 = f"{hours}:{minutes:02d} hours before the start"
    elif arrival_time > exam_time and arrival_time < exam_time + 60:
        output2 = f"{arrival_time - exam_time} minutes after the start"
    elif arrival_time >= exam_time + 60:
        hours = (arrival_time - exam_time) // 60
        minutes = (arrival_time - exam_time) % 60
        output2 = f"{hours}:{minutes:02d} hours after the start"

else: pass

print(output1)
print(output2)
