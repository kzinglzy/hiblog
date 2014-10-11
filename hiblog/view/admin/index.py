#!/usr/bin/env python
# coding: utf-8
from _base.app import Route
from _base.my_view import AdminView


route = Route(prefix='/admin')


@route('/?')
class Index(AdminView):

    def get(self):
        pass


@route('/logout')
class Logout(AdminView):

    def get(self):
        pass
