<template>	
	<view>
		<swiper-tab-head 
		:tabBars="tabBars" 
		:tabIndex="tabIndex" 
		@tabtap="tabtap">
		</swiper-tab-head>
		
		<view class="uni-tab-bar">
			<swiper class="swiper-box" 
			:style="{height:swiperHeight+'px'}" 
			:current="tabIndex" 
			@change="tabChange">
				<swiper-item v-for="(items,index) in newslist" :key='index'>
					<scroll-view scroll-y class="list" @scrolltolower="loadMore(index)">
						<template v-if="items.list.length > 0">
							<!-- 图文，视频列表 -->
							<block v-for="(item, index1) in items.list" :key="index1">
								<index-list :item="item" :index="index1"></index-list>
							</block>
							<!-- 上拉加载 -->
							<load-more :loadText="items.loadText"></load-more>
						</template>
						<template v-else>
							<!-- 无内容默认 -->
							<noThing></noThing>
						</template>
					</scroll-view>
				</swiper-item>
			</swiper>
		</view>
		
	</view>
</template>

<script>
	import indexList from "../../components/index/index-list.vue"
	import swiperTabHead from "../../components/index/swiper-tab-head.vue"
	import loadMore from "../../components/common/load-more.vue"
	import noThing from "../../components/common/no-thing.vue"
	
	export default {
		components: {
			indexList,
			swiperTabHead,
			loadMore,
			noThing
		},
		data() {
			return {
				swiperHeight: 500,
				tabIndex: 0,
				tabBars: [
					{ name: "关注", id: "guanzhu" },
					{ name: "推荐", id: "tuijian" },
					{ name: "体育", id: "tiyu" },
					{ name: "热点", id: "redian" },
					{ name: "财经", id: "caijing" },
					{ name: "娱乐", id: "yule" }
				],
				newslist: [
					{
						loadText: "上拉加载更多",
						list: [
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
						]
					},
					{
						loadText: "上拉加载更多",
						list: [
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
						]
					},
					{
						loadText: "上拉加载更多",
						list: [
							// {
							// 	userpic: "../../static/demo/userpic/12.jpg",
							// 	username: "昵称",
							// 	isguanzhu: true,
							// 	title: "我是标题",
							// 	type: "img",  // img:图文, video:视频
							// 	playnum: null, // 单位:w(万次)
							// 	long: null,
							// 	titlepic: "../../static/demo/datapic/11.jpg",
							// 	infonum: {
							// 		index: 1,  // 0:没有操作, 1:顶, 2:踩
							// 		dingnum: 11,
							// 		cainum: 11
							// 	},
							// 	commentnum: 10,
							// 	sharenum: 10
							// },
							// {
							// 	userpic: "../../static/demo/userpic/12.jpg",
							// 	username: "昵称",
							// 	isguanzhu: false,
							// 	title: "我是标题",
							// 	type: "video",  // img:图文, video:视频
							// 	playnum: "20", // 单位:w(万次)
							// 	long: "2:47",
							// 	titlepic: "../../static/demo/datapic/11.jpg",
							// 	infonum: {
							// 		index: 2,  // 0:没有操作, 1:顶, 2:踩
							// 		dingnum: 11,
							// 		cainum: 11
							// 	},
							// 	commentnum: 10,
							// 	sharenum: 10
							// }
						]
					},
					{
						loadText: "上拉加载更多",
						list: [
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
						]
					},
					{
						loadText: "上拉加载更多",
						list: [
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
						]
					},
					{
						loadText: "上拉加载更多",
						list: [
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
						]
					}
				]
			}
		},
		onLoad() {
			uni.getSystemInfo({
				success: (res) => {
					this.swiperHeight = res.windowHeight - uni.upx2px(100)
				}
			})
		},
		// 监听搜索框点击事件
		onNavigationBarSearchInputClicked() {
			uni.navigateTo({
				url: '../search/search'
			});
		},
		// 监听原生标题导航按钮点击事件
		onNavigationBarButtonTap(e) {
			switch (e.index){
				case 1:
				// 打开发布页面
				uni.navigateTo({
					url: '../add-input/add-input'
				});
					break;
			}
		},
		methods: {
			// 上拉加载
			loadMore(index) {
				if (this.newslist[index].loadText != "上拉加载更多") {
					return;
				}
				// 修改状态
				this.newslist[index].loadText = "加载中...";
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
					this.newslist[index].list.push(obj);
					this.newslist[index].loadText = "上拉加载更多";
				}, 1000)
				// this.newslist[index].loadText = "没有更多数据了";
			},
			// tabbar点击事件
			tabtap(index) {
				this.tabIndex = index;
			},
			// 滑动事件
			tabChange(e) {
				this.tabIndex = e.detail.current;
			}
		},
	}
</script>

<style>

</style>
