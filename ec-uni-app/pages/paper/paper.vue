<template>
	<view class="body">
		<!-- 操作菜单 -->
		<paper-left-popup 
		:show="show"
		@hide="hidepopup"
		@addfriend="addfriend"
		@clear="clear"
		>
		</paper-left-popup>
		<!-- 小纸条列表 -->
		<block v-for="(item, index) in list" :key="index">
			<paper-list :item="item" :index="index"></paper-list>
		</block>
		<!-- 上拉加载 -->
		<load-more :loadText="loadText"></load-more>
	</view>
</template>

<script>
	import paperList from "../../components/paper/paper-list.vue"
	import loadMore from "../../components/common/load-more.vue"
	import paperLeftPopup from "../../components/paper/paper-left-popup.vue"

	export default {
		components: {
			paperList,
			loadMore,
			paperLeftPopup
		},
		data() {
			return {
				show: false,
				loadText: "上拉加载更多",
				list: [
					{
						userpic: "../../static/demo/userpic/12.jpg",
						username: "JIA一勺",
						time: "20:21",
						data: "赵丽颖《知否》一句话打脸，“读书...",
						notenum: "5"
					},
					{
						userpic: "../../static/demo/userpic/12.jpg",
						username: "JIA一勺",
						time: "20:21",
						data: "赵丽颖《知否》一句话打脸，“读书...",
						notenum: "0"
					},
					{
						userpic: "../../static/demo/userpic/12.jpg",
						username: "JIA一勺",
						time: "20:21",
						data: "赵丽颖《知否》一句话打脸，“读书...",
						notenum: "10"
					},
					{
						userpic: "../../static/demo/userpic/12.jpg",
						username: "JIA一勺",
						time: "20:21",
						data: "赵丽颖《知否》一句话打脸，“读书...",
						notenum: "0"
					},
					{
						userpic: "../../static/demo/userpic/12.jpg",
						username: "JIA一勺",
						time: "20:21",
						data: "赵丽颖《知否》一句话打脸，“读书...",
						notenum: "19"
					},
					{
						userpic: "../../static/demo/userpic/12.jpg",
						username: "JIA一勺",
						time: "20:21",
						data: "赵丽颖《知否》一句话打脸，“读书...",
						notenum: "45"
					},
					{
						userpic: "../../static/demo/userpic/12.jpg",
						username: "JIA一勺",
						time: "20:21",
						data: "赵丽颖《知否》一句话打脸，“读书...",
						notenum: "45"
					},
					{
						userpic: "../../static/demo/userpic/12.jpg",
						username: "JIA一勺",
						time: "20:21",
						data: "赵丽颖《知否》一句话打脸，“读书...",
						notenum: "45"
					},
					{
						userpic: "../../static/demo/userpic/12.jpg",
						username: "JIA一勺",
						time: "20:21",
						data: "赵丽颖《知否》一句话打脸，“读书...",
						notenum: "45"
					},
					{
						userpic: "../../static/demo/userpic/12.jpg",
						username: "JIA一勺",
						time: "20:21",
						data: "赵丽颖《知否》一句话打脸，“读书...",
						notenum: "45"
					},
					{
						userpic: "../../static/demo/userpic/12.jpg",
						username: "JIA一勺",
						time: "20:21",
						data: "赵丽颖《知否》一句话打脸，“读书...",
						notenum: "45"
					}
				]
			}
		},
		// 监听下拉刷新
		onPullDownRefresh() {
			this.getdata();
		},
		onReachBottom() {
			this.loadMore();
		},
		// 监听导航按钮点击事件
		onNavigationBarButtonTap(e) {
			switch (e.index){
				case 0:
				uni.navigateTo({
					url: '../user-list/user-list'
				});
				this.hidepopup();
					break;
				case 1:
				console.log("点击了右边按钮");
				this.showpopup();
					break;
			}
		},
		methods: {
			addfriend() {
				console.log("加糗友");
				this.hidepopup();
			},
			clear() {
				console.log("清除缓存");
				this.hidepopup();
			},
			hidepopup() {
				console.log("隐藏弹出框");
				this.show = false;
			},
			showpopup() {
				this.show = true;
			},
			loadMore() {
				if (this.loadText != "上拉加载更多") {
					return;
				}
				// 修改状态
				this.loadText = "加载中...";
				// 获取数据
				setTimeout( () => {
					// 获取完成
					let obj = {
						userpic: "../../static/demo/userpic/12.jpg",
						username: "JIA一勺",
						time: "20:21",
						data: "赵丽颖《知否》一句话打脸，“读书...",
						notenum: "45"
					};
					this.list.push(obj);
					this.loadText = "上拉加载更多";
				}, 1000)
				// this.loadText = "没有更多数据了";
			},
			// 获取数据
			getdata() {
				setTimeout( () => {
					// 服务器获取数据
					let arr = [
						{
							userpic: "../../static/demo/userpic/12.jpg",
							username: "JIA1111",
							time: "20:21",
							data: "赵丽颖《知否》一句话打脸，“读书...",
							notenum: "5"
						},
						{
							userpic: "../../static/demo/userpic/12.jpg",
							username: "JIA2222",
							time: "20:21",
							data: "赵丽颖《知否》一句话打脸，“读书...",
							notenum: "0"
						},
						{
							userpic: "../../static/demo/userpic/12.jpg",
							username: "JIAJIA2222",
							time: "20:21",
							data: "赵丽颖《知否》一句话打脸，“读书...",
							notenum: "10"
						},
						{
							userpic: "../../static/demo/userpic/12.jpg",
							username: "JIA2222一勺",
							time: "20:21",
							data: "赵丽颖《知否》一句话打脸，“读书...",
							notenum: "0"
						},
						{
							userpic: "../../static/demo/userpic/12.jpg",
							username: "JIA2222一勺",
							time: "20:21",
							data: "赵丽颖《知否》一句话打脸，“读书...",
							notenum: "19"
						},
						{
							userpic: "../../static/demo/userpic/12.jpg",
							username: "JIA2222一勺",
							time: "20:21",
							data: "赵丽颖《知否》一句话打脸，“读书...",
							notenum: "45"
						},
						{
							userpic: "../../static/demo/userpic/12.jpg",
							username: "JIA2222一勺",
							time: "20:21",
							data: "赵丽颖《知否》一句话打脸，“读书...",
							notenum: "45"
						},
						{
							userpic: "../../static/demo/userpic/12.jpg",
							username: "JIA一勺",
							time: "20:21",
							data: "赵丽颖《知否》一句话打脸，“读书...",
							notenum: "45"
						},
						{
							userpic: "../../static/demo/userpic/12.jpg",
							username: "JIA一勺",
							time: "20:21",
							data: "赵丽颖《知否》一句话打脸，“读书...",
							notenum: "45"
						},
						{
							userpic: "../../static/demo/userpic/12.jpg",
							username: "JIA一勺",
							time: "20:21",
							data: "赵丽颖《知否》一句话打脸，“读书...",
							notenum: "45"
						},
						{
							userpic: "../../static/demo/userpic/12.jpg",
							username: "JIA一勺",
							time: "20:21",
							data: "赵丽颖《知否》一句话打脸，“读书...",
							notenum: "45"
						}
					]
					// 赋值
					this.list = arr;
					// 关闭下拉刷新
					uni.stopPullDownRefresh();
				}, 2000);
				
				
			}
		}
	}
</script>

<style>
	.body {
		padding: 0 20rpx;
	}
</style>
