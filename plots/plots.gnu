set datafile separator ','
set grid
set term png

# bus
set title 'Bus'
set xlabel 'Time (0.01 s)'
set ylabel 'Acceleration (m/s^2)'
set output 'bus.png'
plot '../data/bus.csv' using 0:1 title 'X' with lines, \
     '../data/bus.csv' using 0:2 title 'Y' with lines, \
     '../data/bus.csv' using 0:3 title 'Z' with lines

# dancing
set title 'Dancing'
set xlabel 'Time (0.01 s)'
set ylabel 'Acceleration (m/s^2)'
set output 'dancing.png'
plot '../data/dancing.csv' using 0:1 title 'X' with lines, \
     '../data/dancing.csv' using 0:2 title 'Y' with lines, \
     '../data/dancing.csv' using 0:3 title 'Z' with lines

# stairs
set title 'Stairs'
set xlabel 'Time (0.01 s)'
set ylabel 'Acceleration (m/s^2)'
set output 'stairs.png'
plot '../data/stairs.csv' using 0:1 title 'X' with lines, \
     '../data/stairs.csv' using 0:2 title 'Y' with lines, \
     '../data/stairs.csv' using 0:3 title 'Z' with lines

# running
set title 'Running'
set xlabel 'Time (0.01 s)'
set ylabel 'Acceleration (m/s^2)'
set output 'running.png'
plot '../data/running.csv' using 0:1 title 'X' with lines, \
     '../data/running.csv' using 0:2 title 'Y' with lines, \
     '../data/running.csv' using 0:3 title 'Z' with lines

# walking
set title 'Walking'
set xlabel 'Time (0.01 s)'
set ylabel 'Acceleration (m/s^2)'
set output 'walking.png'
plot '../data/walking.csv' using 0:1 title 'X' with lines, \
     '../data/walking.csv' using 0:2 title 'Y' with lines, \
     '../data/walking.csv' using 0:3 title 'Z' with lines

