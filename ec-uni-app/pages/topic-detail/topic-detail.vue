<template>
	<view>
		<!-- 话题介绍 -->
		<topic-info :item="topicInfo"></topic-info>
		<!-- tabbar切换 -->
		<swiper-tab-head
		:tabBars="tabBars" 
		:tabIndex="tabIndex" 
		@tabtap="tabtap"
		scrollStyle="border-bottom: 0"
		scrollItemStyle="width: 50%">
		</swiper-tab-head>
		<!-- 列表 -->
		<view class="topic-detail-list">
			<block v-for="(listitem, listindex) in tablist[tabIndex].list" :key="listindex">
				<common-list :item="listitem" :index="listindex"></common-list>
			</block>
			<!-- 上拉加载 -->
			<load-more :loadText="tablist[tabIndex].loadText"></load-more>
		</view>
	</view>
</template>

<script>
	import topicInfo from "../../components/topic/topic-info.vue"
	import swiperTabHead from "../../components/index/swiper-tab-head.vue"
	import commonList from "../../components/common/common-list.vue"
	import loadMore from "../../components/common/load-more.vue"
	
	export default {
		components: {
			topicInfo,
			swiperTabHead,
			commonList,
			loadMore
		},
		data() {
			return {
				topicInfo: {
					titlepic: "../../static/demo/topicpic/13.jpeg",
					title: "忆往事，敬余生",
					desc: "面试官：在电梯里巧遇马云你会怎么做？90后女孩的回答当初被录用",
					totalnum: 100,
					todaynum: 50
				},
				tabIndex: 0,
				tabBars: [
					{ name: "默认", id: "moren" },
					{ name: "最新", id: "zuixin" },
				],
				tablist: [
					{
						loadText: "上拉加载更多",
						list: [
							// 文字
							{
								userpic: "../../static/demo/userpic/12.jpg",
								username: "哈哈",
								sex: 0,  // 0 男, 1 女
								age: 25,
								isguanzhu: false,
								title: "我是文字",
								titlepic: "",
								video: false,
								share: false,
								path: "深圳 龙岗",
								sharenum: 20,
								commentnum: 30,
								goodnum: 20
							},
							// 图文
							{
								userpic: "../../static/demo/userpic/12.jpg",
								username: "哈哈",
								sex: 0,  // 0 男, 1 女
								age: 25,
								isguanzhu: false,
								title: "我是图文",
								titlepic: "../../static/demo/datapic/13.jpg",
								video: false,
								share: false,
								path: "深圳 龙岗",
								sharenum: 20,
								commentnum: 30,
								goodnum: 20
							},
							// 视频
							{
								userpic: "../../static/demo/userpic/12.jpg",
								username: "哈哈",
								sex: 0,  // 0 男, 1 女
								age: 25,
								isguanzhu: false,
								title: "我是视频",
								titlepic: "../../static/demo/datapic/13.jpg",
								video: {
									looknum: 20,  // 单位w(万)
									long: "2:47"
								},
								share: false,
								path: "深圳 龙岗",
								sharenum: 20,
								commentnum: 30,
								goodnum: 20
							},
							// 分享
							{
								userpic: "../../static/demo/userpic/12.jpg",
								username: "哈哈",
								sex: 0,  // 0 男, 1 女
								age: 25,
								isguanzhu: false,
								title: "我是分享",
								titlepic: "",
								video: false,
								share: {
									title: "分享标题",
									titlepic: "../../static/demo/datapic/14.jpg"
								},
								path: "深圳 龙岗",
								sharenum: 20,
								commentnum: 30,
								goodnum: 20
							}
						]
					},
					{
						loadText: "上拉加载更多",
						list: [
							// 文字
							{
								userpic: "../../static/demo/userpic/9.jpg",
								username: "嘿嘿",
								sex: 0,  // 0 男, 1 女
								age: 25,
								isguanzhu: false,
								title: "我是文字",
								titlepic: "",
								video: false,
								share: false,
								path: "深圳 龙岗",
								sharenum: 20,
								commentnum: 30,
								goodnum: 20
							},
							// 图文
							{
								userpic: "../../static/demo/userpic/9.jpg",
								username: "嘿嘿",
								sex: 0,  // 0 男, 1 女
								age: 25,
								isguanzhu: false,
								title: "我是图文",
								titlepic: "../../static/demo/datapic/14.jpg",
								video: false,
								share: false,
								path: "深圳 龙岗",
								sharenum: 20,
								commentnum: 30,
								goodnum: 20
							},
							// 视频
							{
								userpic: "../../static/demo/userpic/9.jpg",
								username: "嘿嘿",
								sex: 0,  // 0 男, 1 女
								age: 25,
								isguanzhu: false,
								title: "我是视频",
								titlepic: "../../static/demo/datapic/14.jpg",
								video: {
									looknum: 20,  // 单位w(万)
									long: "2:47"
								},
								share: false,
								path: "深圳 龙岗",
								sharenum: 20,
								commentnum: 30,
								goodnum: 20
							},
							// 分享
							{
								userpic: "../../static/demo/userpic/9.jpg",
								username: "嘿嘿",
								sex: 0,  // 0 男, 1 女
								age: 25,
								isguanzhu: false,
								title: "我是分享",
								titlepic: "",
								video: false,
								share: {
									title: "分享标题",
									titlepic: "../../static/demo/datapic/11.jpg"
								},
								path: "深圳 龙岗",
								sharenum: 20,
								commentnum: 30,
								goodnum: 20
							}
						]
					},
				]
			}
		},
		onReachBottom() {
			this.loadMore();
		},
		// 监听下拉刷新
		onPullDownRefresh() {
			this.getdata();
		},
		methods: {
			// 上拉刷新
			getdata() {
				// 关闭下拉刷新
				setTimeout( () => {
					// 获取数据
					let arry = [
								// 文字
								{
									userpic: "../../static/demo/userpic/9.jpg",
									username: "嘻嘻",
									sex: 0,  // 0 男, 1 女
									age: 25,
									isguanzhu: false,
									title: "我是文字嘻嘻",
									titlepic: "",
									video: false,
									share: false,
									path: "深圳 龙岗",
									sharenum: 20,
									commentnum: 30,
									goodnum: 20
								},
								// 图文
								{
									userpic: "../../static/demo/userpic/9.jpg",
									username: "嘻嘻",
									sex: 0,  // 0 男, 1 女
									age: 25,
									isguanzhu: false,
									title: "我是图文嘻嘻",
									titlepic: "../../static/demo/datapic/14.jpg",
									video: false,
									share: false,
									path: "深圳 龙岗",
									sharenum: 20,
									commentnum: 30,
									goodnum: 20
								},
								// 视频
								{
									userpic: "../../static/demo/userpic/9.jpg",
									username: "嘻嘻",
									sex: 0,  // 0 男, 1 女
									age: 25,
									isguanzhu: false,
									title: "我是视频嘻嘻",
									titlepic: "../../static/demo/datapic/14.jpg",
									video: {
										looknum: 20,  // 单位w(万)
										long: "2:47"
									},
									share: false,
									path: "深圳 龙岗",
									sharenum: 20,
									commentnum: 30,
									goodnum: 20
								},
								// 分享
								{
									userpic: "../../static/demo/userpic/9.jpg",
									username: "嘻嘻",
									sex: 0,  // 0 男, 1 女
									age: 25,
									isguanzhu: false,
									title: "我是分享嘻嘻",
									titlepic: "",
									video: false,
									share: {
										title: "分享标题",
										titlepic: "../../static/demo/datapic/11.jpg"
									},
									path: "深圳 龙岗",
									sharenum: 20,
									commentnum: 30,
									goodnum: 20
								}
							];
					// 赋值
					this.tablist[this.tabIndex].list = arry;
					uni.stopPullDownRefresh();
				}, 2000);
			},
			// 上拉加载
			loadMore() {
				if (this.tablist[this.tabIndex].loadText != "上拉加载更多") {
					return;
				}
				// 修改状态
				this.tablist[this.tabIndex].loadText = "加载中...";
				// 获取数据
				setTimeout( () => {
					// 获取完成
					let obj = {
						userpic: "../../static/demo/userpic/12.jpg",
						username: "哈哈",
						sex: 0,  // 0 男, 1 女
						age: 25,
						isguanzhu: false,
						title: "我是图文",
						titlepic: "../../static/demo/datapic/13.jpg",
						video: false,
						share: false,
						path: "深圳 龙岗",
						sharenum: 20,
						commentnum: 30,
						goodnum: 20
					};
					this.tablist[this.tabIndex].list.push(obj);
					this.tablist[this.tabIndex].loadText = "上拉加载更多";
				}, 1000)
				// this.tablist[this.tabIndex].loadText = "没有更多数据了";
			},
			// tabbar点击事件
			tabtap(index) {
				this.tabIndex = index;
			}
		}
	}
</script>

<style>
</style>
