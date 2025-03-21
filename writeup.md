## Question 1

Take a look at the file labeled `data/phase0.txt`. Why might we have missing values or values that state "NO DATA" in this dataset? While we are currently ignoring these values, what might be the risk of filtering these values out?

The device could be off or the participant was not wearing the device at the time. Since the file does not have timestamps and we use the row number as the heart rate captured at a time, when we filter out non-valid value rows and store the numbers into a continuous list, we can end up having an inaccurate depiction of the overall heart rate changes.

## Question 2

During sleep, we expect maximum heart rate of a phase to be **lower** than the maximum heart rate of all other phases. Observe the visualizations and descriptive statistics that you've calculated. Using these findings, in which phase does sleep occur? Mention numerical details that back your findings.

Based on the graphs, Phase 0 and Phase 3 are the most likely candidates for when the sleep occured because the heart rates in those phases are relatively lower. However, if there can only be one sleeping phase, based on the expectation that maximum heart rate during sleeping phase is lower than the maximum heart rate of all other phases, it will be Phase 0 since its max heart is 93 while Phase 3's maximum is 99.

## Question 3

During exercise, we expect the maximum heart rate of a phase to be **higher** the maximum heart rate of all other phases. Observe the visualizations and descriptive statistics that you've calculated. Using these findings, in which phase(s) does exercise occur? Mention numerical details that back your findings. 

Phase 1 and Phase 2 both have higher heart rates. However, if we compares the maximum heart rates: 110 for Phase 1 and 117 for Phase 2, we see that Phase 2's value is higher. Therefore, based on the expectation that maximum heart rate during exercise is lower than the maximum heart rate of all other phases, Phase 2 is most likely the exercise phase.

## Question 4

During regular periods of awake activity, we expect the average heart rate of a phase to be relatively **lower** than the average heart rate of other phases, but we also expect standard deviation to be **higher**. In which phase do we notice this trend?

In Phase 3, we noticed it has the lowest average heart rate, but it has a higher standard deviation. Therefore, Phase 3 is most likely the regular period of awake activity.