def mergeMeetings(meetings):
    meetings = sorted(meetings)

    merged_meetings = [meetings[0]]

    for meeting in meetings[1:]:
        last_merged = merged_meetings[-1]

        if meeting[0] <= last_merged[1]:
            merged_meeting = (last_merged[0],max(last_merged[1],meeting[1]))
            merged_meetings[-1] = merged_meeting
        else:
            merged_meetings.append(meeting)

    return merged_meetings
