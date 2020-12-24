# SELF REPLICATING SCRIPT

## A simple self-replicating script produced in python.

What it does can be summarized as follows:
1. Store all its code
1. Select the py and pyw scripts *(in the same folder)* that have not yet been infected
1. Appends the code from step 1 to the end of each script from step 2

### Note:
The functionality of the victim scripts is not compromised in any way; like a biological virus, to obtain a greater number of infected, the self-replicating script also exploits the host's activity to achieve its goal (AKA replicate itself).
And, in this case, wish everyone a Merry Christmas

### Consideration:
For the purpose of non-detection of the self-replicating script by the user, it would be advisable to delegate the execution of the payload to a second thread

***

## How to Reproduce:
1. clone the repo
2. (optional) add as many `victim.py` files you like
3. in terminal digit `pithon3 self_replicating_script.py`

Now all the `.py` scripts in same folder are *infected*. Add another victim and have it infected with a previously infected fellow

***

#### Credits:
[video](https://www.youtube.com/watch?v=qNy_amMuVZQ)