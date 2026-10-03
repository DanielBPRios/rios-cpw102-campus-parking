# Engineering Design

**Project:** Campus Parking Helper  
**Team members:**  Daniel Rios
**Date:** 2 October 2026

## Problem Summary

The problem is that students and visitors have trouble calculating the costs all on their own. They are concerned that they will make innacurate mistakes when trying to calculate (1) parking costs and (2) the total number of hours, which includes partial hours. 

While the parking costs may be the same, if there is no system in place to read their parked hours, students and visitors may (1) calculate their hours incorrectly or (2) not understand how to calculate minutes into the correct hours.

## Proposed solution

My proposed solution is to create a simple calculation for the independent variable (the Parking Costs) and the dependent variable (the Parked Hours). 

However, due to accessibility, since we cannot assume that the user can correctly calculate their minutes into hours or own a calculator/phone to make an accurate calculation for them, there must be another solution to help combat user confusion, which is making the user input minutes rather than percentages of hours, which they could calculate incorrectly. 

After giving the program their minutes parked, the program will then feed this data into its functions that will convert it into hours, then put it into its normal multiplication function to calculate the total costs. 

## Technical design

### Inputs
_What data and information will go into the program? What data types will the program use to represent that data?_

**p_hours** (float): user entered anticipated number of hours they park

**OR**

**parked_minutes** (integer): user entered anticipated number of minutes they park

### Processing
_What will the program do with the data? What calculations will it perform?_ 


est_cost = cost per hour * parked hours
est_cost = 2 * 2.5

### Output
_What will the program return or print to the user?_

**est_cost** = print

### Functions
_What function(s) could this program use to modularize the logic? What actions belong together?_

get user inputs
(accessibility) calculate the minutes into hours
calculate the costs
print to the user

## Example interaction

```text
User input: 

Program output:
```

## Implementation plan

1. Get user minutes via input functions.
2. Calculate minutes into hours via / symbol and assigning that value to a variable.
3. Apply the hour(s) variable into the calculation function to then get the total estimated costs for parking.
4. Print the total costs clearly to the user.

