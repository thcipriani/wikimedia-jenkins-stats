#!/bin/bash

printf '%b' 'https://graphite.wikimedia.org/render/?from=-24hours'
printf '%b' '&width=400'
printf '%b' '&height=180'
printf '%b' '&target=alias(averageSeries(zuul.pipeline.*.job.*.wait_time.mean),%27Average%20hourly%20wait%20time%27)'
printf '%b' '&target=alias(maxSeries(zuul.pipeline.*.job.*.wait_time.upper),%27Max%20hourly%20wait%20time%27)'
printf '%b' '&lineMode=connected'
printf '%b' '&yUnitSystem=msec'
printf '%b' '&title=Job%20Wait%20Time'
