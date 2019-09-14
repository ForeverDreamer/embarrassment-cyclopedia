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
						<!-- 图文，视频列表 -->
						<block v-for="(item, index1) in items.list" :key="index1">
							<index-list :item="item" :index="index1"></index-list>
						</block>
						<!-- 上拉加载 -->
						<view class="load-more">{{items.loadText}}</view>
					</scroll-view>
				</swiper-item>
			</swiper>
		</view>
		
	</view>
</template>

<script>
	import indexList from "../../components/index/index-list.vue"
	import swiperTabHead from "../../components/index/swiper-tab-head.vue"
	
	export default {
		components: {
			indexList,
			swiperTabHead
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
	.load-more {
		text-align: center;
		color: #AAAAAA;
		padding: 15upx;
	}
</style>
