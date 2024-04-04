
import moviepy.editor as mpe


# Load the video file
clip = mpe.VideoFileClip("/Users/aditya/Desktop/potat1/lop/bw.mp4")

# Get the duration of the video
duration = clip.duration

# Calculate the number of 5-second segments
num_segments = int(duration *10)

# Create a list of 5-second segments
segments = []
for i in range(num_segments):
    start_time = i /10
    end_time = (i + 1) /10
    segment = clip.subclip(start_time, end_time)
    segments.append(segment)

# Export each segment to a new video file
for i, segment in enumerate(segments):
    segment.write_videofile("segment_{}.mp4".format(i))