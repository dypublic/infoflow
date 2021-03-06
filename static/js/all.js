﻿function check_empty() {
	var inputs = document.getElementById("post_new");
	for (var i = 0; i < inputs.length; i++) {
		if (inputs.elements[i].type == "text") {
			if (inputs.elements[i].value == '') {
				return false;
			} else {
				return true;
			}
		}
	}
}


/*
 <style type="text/css">
 body{
  margin: 0;
  padding: 0;
  font-size: 14px;
  font-family: tahoma, arial;
  background: #fff;
 }
.PagerView{
 color: #333;
 text-align: center;
 margin: 8px;
}
.PagerView span{
 color: #999;
 margin: 0 1px;
 padding: 3px 6px;
 border: 1px solid #ccc;
}
.PagerView span.on{
 color: #333;
 font-weight: bold;
 border: 1px solid #333;
}
.PagerView a{
 color: #00f;
 text-decoration: none;
}
.PagerView a span{
 border: 1px solid #66c;
 color: #33f;
}
.PagerView a:hover span{
 color: #f00;
 background: #ff9;
}
 </style>*/

/**
 * 开源代码, 有兴趣的可以在保留声明的前提下免费使用.
 *********** 声明开始 ***********
 * @author ideawu@163.com
 * @link http://www.ideawu.net
 *********** 声明结束 ***********
 *
 * 分页控件, 使用原生的JavaScript代码编写. 重写onclick方法, 获取翻页事件,
 * 可用来向服务器端发起AJAX请求.
 *
 * 示例:
 * HTML:
 * <div id="pager"></div>
 *
 * JavaScript:
 * var pager = new PagerView('pager');
 * pager.index = 3; // 当前是第3页
 * pager.size = 16; // 每页显示16条记录
 * pager.itemCount = 100; // 一共有100条记录
 *
 * pager.onclick = function(index){
 * alert('click on page: ' + index);
 * // display data...
 * pager.render();
 * };
 *
 * pager.render();
 *
 * @param id: HTML节点的id属性值, 控件将显示在该节点中. 可以延迟到render方法调用之前设置.
 */

function PagerView(id) {
	var self = this;
	this.id = id;
	this.container = null;
	this.index = 1;
	// 当前页码, 从1开始
	this.size = 15;
	// 每页显示记录数
	this.maxButtons = 9;
	// 显示的分页按钮数量
	this.itemCount = 0;
	// 记录总数
	this.pageCount = 0;
	// 总页数
	/**
	 * 控件使用者重写本方法, 获取翻页事件, 可用来向服务器端发起AJAX请求.
	 * @param index: 被点击的页码.
	 */
	this.onclick = function(index) {
	};
	/**
	 * 内部方法.
	 */
	this._onclick = function(index) {
		self.index = index;
		self.onclick(index);
		self.render();
	};
	/**
	 * 在显示之前计算各种页码变量的值.
	 */
	this.calculate = function() {
		self.pageCount = parseInt(Math.ceil(self.itemCount / self.size));
		self.index = parseInt(self.index);
		if (self.index > self.pageCount) {
			self.index = self.pageCount;
		}
	};
	/**
	 * 渲染分页控件.
	 */
	this.render = function() {
		if (self.id != undefined) {
			var div = document.getElementById(self.id);
			div.view = self;
			self.container = div;
		}
		self.calculate();
		var start, end;
		start = Math.max(1, self.index - parseInt(self.maxButtons / 2));
		end = Math.min(self.pageCount, start + self.maxButtons - 1);
		start = Math.max(1, end - self.maxButtons + 1);
		var str = "";
		str += "<div class=\"PagerView\">\n";
		if (self.pageCount > 1) {
			if (self.index != 1) {
				str += '<a href="/1"><span>|<</span></a>';
				str += '<a href="javascript://' + (self.index - 1) + '"><span><<</span></a>';
			} else {
				str += '<span>|<</span>';
				str += '<span><<</span>';
			}
		}
		for (var i = start; i <= end; i++) {
			if (i == this.index) {
				str += '<span class="on">' + i + "</span>";
			} else {
				str += '<a href="javascript://' + i + '"><span>' + i + "</span></a>";
			}
		}
		if (self.pageCount > 1) {
			if (self.index != self.pageCount) {
				str += '<a href="javascript://' + (self.index + 1) + '"><span>>></span></a>';
				str += '<a href="javascript://' + self.pageCount + '"><span>>|</span></a>';
			} else {
				str += '<span>>></span>';
				str += '<span>>|</span>';
			}
		}
		str += ' 一共' + self.pageCount + '页, ' + self.itemCount + '条记录 ';
		str += "</div><!-- /.pagerView -->\n";
		self.container.innerHTML = str;
		var a_list = self.container.getElementsByTagName('a');
		for (var i = 0; i < a_list.length; i++) {
			a_list[i].onclick = function() {
				var index = this.getAttribute('href');
				if (index != undefined && index != '') {
					index = parseInt(index.replace('javascript://', ''));
					self._onclick(index)
				}
				return false;
			};
		}
	};
}
