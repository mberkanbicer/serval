###############################################################################
#
# Copyright (c) 2010 Ruslan Spivak
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
###############################################################################

__author__ = 'Ruslan Spivak <ruslan.spivak@gmail.com>'

from serval.model import Symbol, EmptyList
from serval.expression.util import (
    is_tagged_list, cons, cdr, cadr, cddr, caar, cadar)


def is_let_binding(expr):
    return is_tagged_list(expr, Symbol('let'))

def binding_variables(expr):
    def inner(expr):
        if expr is EmptyList:
            return EmptyList
        return cons(caar(expr), inner(cdr(expr)))

    return inner(cadr(expr))

def binding_values(expr):
    def inner(expr):
        if expr is EmptyList:
            return EmptyList
        return cons(cadar(expr), inner(cdr(expr)))

    return inner(cadr(expr))

def binding_body(expr):
    return cddr(expr)
