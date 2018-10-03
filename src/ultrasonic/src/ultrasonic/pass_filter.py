#!/usr/bin/env python
# encoding: utf-8


class PassFilter:
    def __init__(self, threshold, alpha=0.001):
        self.first_time = True
        self.threshold = threshold
        self.alpha = alpha
        self.last_val = 0.0

    def filter(self, val):
        if val >= self.threshold:
            return self.threshold
        if self.first_time:
            self.first_time = False
        else:
            val = val * self.alpha + self.last_val * (1 - self.alpha)
        self.last_val = val
        return val
