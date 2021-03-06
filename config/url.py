#!/usr/bin/env python
# coding: utf-8

pre_fix = 'controllers.'

urls = (
    '/',                    pre_fix + 'todo.Index',
    '/todo/new',            pre_fix + 'todo.New',
    '/todo/(\d+)',          pre_fix + 'todo.View',
    '/todo/(\d+)/edit',     pre_fix + 'todo.Edit',
    '/todo/(\d+)/delete',   pre_fix + 'todo.Delete',
    '/todo/(\d+)/finish',   pre_fix + 'todo.Finish',
    '/todo/topic/(\d+)/edit',     pre_fix + 'todo.TopicEdit',
    '/todo/item/(\d+)/edit',     pre_fix + 'todo.ItemEdit',
    '/todo/item/(\d+)/delete',   pre_fix + 'todo.ItemDelete',
    '/todo/item/new',            pre_fix + 'todo.ItemNew',
    '/todo/page/(\d+)',            pre_fix + 'todo.Page',
)
