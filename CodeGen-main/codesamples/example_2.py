def _eval_is_subset(self, other):
    if isinstance(other, PowerSet):
        return self.arg.is_subset(other.arg)


