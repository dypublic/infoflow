#!/usr/bin/env python
# coding: utf-8
import web
from config import settings
from datetime import datetime

render = settings.render
db = settings.db
tb = 'todo'
tb_topic = 'topics'
tb_items = 'items'
page_items = 20
def get_by_id(id):
    s = db.select(tb, where='id=$id', vars=locals())
    if not s:
        return False
    return s[0]

def get_topic_by_id(id):
    s = db.select(tb_topic, where='id=$id', vars=locals())
    if not s:
        return False
    return s[0]

def get_items_by_topic_id(id):
    s = db.select(tb_items,  where='topic_id=$id', order='post_date asc', vars=locals())
    if not s:
        return False
    return s

def get_item_by_id(id):
    s = db.select(tb_items,  where='id=$id', vars=locals())
    if not s:
        return False
    return s[0]

class New:

    def POST(self):
        i = web.input()
        title = i.get('title', None)
        creator = i.get('creator', None)
        if not title:
            return render.error('标题是必须的', None)
        db.insert(tb_topic, title=title, creator = creator, post_date=datetime.now())
        print datetime.now()
        raise web.seeother('/')
    


class Finish:

    def GET(self, id):
        todo = get_by_id(id)
        if not todo:
            return render.error('没找到这条记录', None)
        i = web.input()
        status = i.get('status', 'yes')
        if status == 'yes':
            finished = 1
        elif status == 'no':
            finished = 0
        else:
            return render.error('您发起了一个不允许的请求', '/')
        db.update(tb, finished=finished, where='id=$id', vars=locals())
        raise web.seeother('/')


class Edit:

    def GET(self, id):
        topic = get_topic_by_id(id)
        if not topic:
            return render.error('没找到这条记录', None)
        items = get_items_by_topic_id(id)
        if not items: items = []
        return render.todo.edit_topic(topic,items)

    def POST(self, id):
        todo = get_by_id(id)
        if not todo:
            return render.error('没找到这条记录', None)
        i = web.input()
        title = i.get('title', None)
        if not title:
            return render.error('标题是必须的', None)
        db.update(tb, title=title, where='id=$id', vars=locals())
        return render.error('修改成功！', '/')
    
class TopicEdit:

    def GET(self, id):
        topic = get_topic_by_id(id)
        if not topic:
            return render.error('没找到这条记录', None)
        return render.todo.edit(topic)

    def POST(self, id):
        todo = get_topic_by_id(id)
        if not todo:
            return render.error('没找到这条记录', None)
        i = web.input()
        title = i.get('title', None)
        if not title:
            return render.error('标题是必须的', None)
        db.update(tb, title=title, where='id=$id', vars=locals())
        return render.error('修改成功！', '/')
    
class ItemNew:

    def POST(self):
        i = web.input()
        content = i.get('content', None)
        creator = i.get('creator', None)
        topic_id = i.get('topic_id', None)
        if not content:
            return render.error('内容是必须的', None)
        if not topic_id:
            return render.error('主题没找到', None)
        db.insert(tb_items, content=content, topic_id = topic_id,creator = creator, post_date=datetime.now())
        print datetime.now()
        raise web.seeother('/todo/%s/edit'%(topic_id))
    
class ItemEdit:

    def GET(self, id):
        items = get_item_by_id(id)
        if not items:
            return render.error('没找到这条记录', None)
        return render.todo.edit_edit_topic(id,items)

    def POST(self, id):
        item = get_item_by_id(id)
        if not item:
            return render.error('没找到这条记录', None)
        i = web.input()
        content = i.get('content', None)
        if not content:
            return render.error('标题是必须的', None)
        db.update(tb, content=content,where='id=$id', last_date=datetime.now(), vars=locals())
        return render.error('修改成功！', '/')
    
class Delete:

    def GET(self, id):
        todo = get_by_id(id)
        if not todo:
            return render.error('没找到这条记录', None)
        db.delete(tb, where='id=$id', vars=locals())
        return render.error('删除成功！', '/')

class Page:

    def GET(self,page_index):
        count = db.select(tb_topic, what = 'count(id)')
        topics = db.select(tb_topic, order='post_date desc', limit = page_items, offset = (page_index-1)*page_items)
#        for topic in topics:
#            print topic.post_date
        return render.index(topics,page_index,count)
class Index:

    def GET(self):
        result = db.select(tb_topic, what = 'count(id)')
        count = result[0]['count(id)']
        topics = db.select(tb_topic, order='post_date desc', limit = page_items)
#        for topic in topics:
#            print topic.post_date
        return render.index(topics,1,count)