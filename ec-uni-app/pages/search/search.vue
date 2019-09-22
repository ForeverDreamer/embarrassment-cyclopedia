<template>
	<view>
		<template v-if="list.length > 0">
			<!-- 搜索结果 -->
			<block v-for="(item, index) in list" :key="index">
				<index-list :item="item" :index="index"></index-list>
			</block>
			<load-more :loadText="loadText"></load-more>
		</template>
		<template v-else-if="issearch && list.length < 1">
			<!-- 无内容默认 -->
			<noThing></noThing>
		</template>
	</view>
</template>

<script>
	import indexList from "../../components/index/index-list.vue"
	import noThing from "../../components/common/no-thing.vue"
	import loadMore from "../../components/common/load-more.vue"
	
	export default {
		components: {
			indexList,
			noThing,
			loadMore
		},
		data() {
			return {
				issearch: false,
				loadText: "上拉加载更多",
				list: []
			}
		},
		// 监听原生标题导航按钮点击事件
		onNavigationBarButtonTap(e) {
			if (e.index == 0) {
				uni.navigateBack({
					delta: 1
				})
			}
		},
		// 监听搜索框文本变化
		onNavigationBarSearchInputChanged(e) {
			console.log(JSON.stringify(e))
		},
		// 监听点击搜索按钮事件
		onNavigationBarSearchInputConfirmed(e) {
			if (e.text) {
				this.getdata(e.text);
			}
		},
		// 监听页面触底事件
		onReachBottom() {
			this.loadMore();
		},
		methods: {
			// 搜索事件
			getdata(val) {
				// 请求服务器 post
				uni.showLoading({
					title: '加载中...'
				});
				setTimeout( () => {
					let arr = [
						{
							userpic: "../../static/demo/userpic/12.jpg",
							username: "昵称",
							isguanzhu: true,
							title: "我是标题",
							type: "img",  // img:图文, video:视频
							playnum: null, // 单位:w(万次)
							long: null,
							titlepic: "../../static/demo/datapic/11.jpg",
							infonum: {
								index: 1,  // 0:没有操作, 1:顶, 2:踩
								dingnum: 11,
								cainum: 11
							},
							commentnum: 10,
							sharenum: 10
						},
						{
							userpic: "../../static/demo/userpic/12.jpg",
							username: "昵称",
							isguanzhu: false,
							title: "我是标题",
							type: "video",  // img:图文, video:视频
							playnum: "20", // 单位:w(万次)
							long: "2:47",
							titlepic: "../../static/demo/datapic/11.jpg",
							infonum: {
								index: 2,  // 0:没有操作, 1:顶, 2:踩
								dingnum: 11,
								cainum: 11
							},
							commentnum: 10,
							sharenum: 10
						}
					];
					this.list = arr;
					uni.hideLoading();
					this.issearch = true;
				}, 1000)
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
						username: "昵称",
						isguanzhu: true,
						title: "我是标题",
						type: "img",  // img:图文, video:视频
						playnum: null, // 单位:w(万次)
						long: null,
						titlepic: "../../static/demo/datapic/11.jpg",
						infonum: {
							index: 1,  // 0:没有操作, 1:顶, 2:踩
							dingnum: 11,
							cainum: 11
						},
						commentnum: 10,
						sharenum: 10
					};
					this.list.push(obj);
					this.loadText = "上拉加载更多";
				}, 1000)
				// this.loadText = "没有更多数据了";
			}
		}
	}
</script>

<style>

</style>
