#!/user/bin/env python import sys#importing system modules to work with directory files if __name__ == “__main__”:# Starting with an empty dictionary here. Which is termed as the order#. All keys in this dictionary appear as a name, and the specified values for them# will be the number of times that specific name will appear.order = {}# sys.stdin is an object used for files. All those functions applied to
# a file object can also be used for sys. Stdin.

For order in sys.stdin.readlines():

order = order.strip()

If order in orders:

orders[order] += 1

Else:

orders[order] = 1

for order, count in orders.iteritems():

sys.stdout.write(“%d\t%s\n” % (count, order))
