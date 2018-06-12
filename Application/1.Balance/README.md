# Balance calculation

You are handed a nice file of the following format:

```
+50,01/01/2018
-30,01/01/2018
-30,03/01/2018
-30,04/01/2018
+100,31/12/2017
----
01/01/2018
```

Each line is a data point, consisting of two items - transaction & date:

* Date is in the format `dd/mm/yyyy`.
* Transaction is in the format `+amount` or `-amount`. There won't be `amount`.

Transacitons can be positive (you receive money) or negative (you give money).

Implement a program that reads this file from stdin, followed by a special delimiter - `----`, followed by a new line with date.

**Balance is calculated by summing all transactions, sorted by their date.**

Your program should output:

* The balance to the given date.
* Or if there's no record for that date, the closest balance before that date.

A sample input might look like this:

```
+50,01/01/2018
-30,30/12/2017
+100,31/12/2017
----
01/01/2018
````

Your program should output `+120` since the balance at `01/01/2018` is:

* `-30` from `30/12/2017`
* `+100` from `31/12/2017`
* `+50` from `01/01/2018`
* Total sum = `-30 + 100 + 50 = +120`

------

Another example might include more than 1 transaction for a given date:

```
+50,01/01/2018
-30,01/01/2018
-30,03/01/2018
-30,04/01/2018
+100,31/12/2017
----
02/01/2018
```

The output should be `+120` and the date, taken into account - `01/01/2018`.
