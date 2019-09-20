<template>
	<view class="body">
		<!-- tabbar切换 -->
		<swiper-tab-head
		:tabBars="tabBars" 
		:tabIndex="tabIndex" 
		@tabtap="tabtap"
		scrollStyle="border-bottom: 0"
		scrollItemStyle="width: 33%">
		</swiper-tab-head>
		<!-- 好友列表 -->
		<view class="uni-tab-bar">
			<swiper class="swiper-box" 
			:style="{height:swiperHeight+'px'}" 
			:current="tabIndex" 
			@change="tabChange">
				<swiper-item v-for="(items,index) in newslist" :key='index'>
					<scroll-view scroll-y class="list" @scrolltolower="loadMore(index)">
						<template v-if="items.list.length > 0">
							<!-- 好友列表 -->
							<block v-for="(item, index1) in items.list" :key="index1">
								<user-list :item="item" :index="index1"></user-list>
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
	import swiperTabHead from "../../components/index/swiper-tab-head.vue"
	import userList from "../../components/user-list/user-list.vue"
	import loadMore from "../../components/common/load-more.vue"
	import noThing from "../../components/common/no-thing.vue"

	export default {
		components: {
			swiperTabHead,
			userList,
			loadMore,
			noThing
		},
		data() {
			return {
				swiperHeight: 500,
				tabIndex: 0,
				tabBars: [
					{ name: "互关", id: "huguan", num: 10 },
					{ name: "关注", id: "guanzhu", num: 20 },
					{ name: "粉丝", id: "fensi", num: 30 },
				],
				newslist: [
					{
						loadText: "上拉加载更多",
						list: [
							{
								userpic: "../../static/demo/userpic/12.jpg",
								username: "极尔文化",
								age: 20,
								sex: 0,
								isguanzhu: true
							},
							{
								userpic: "../../static/demo/userpic/12.jpg",
								username: "Supzeol",
								age: 30,
								sex: 1,
								isguanzhu: false
							},
							{
								userpic: "../../static/demo/userpic/12.jpg",
								username: "Supzeol",
								age: 30,
								sex: 1,
								isguanzhu: false
							},
							{
								userpic: "../../static/demo/userpic/12.jpg",
								username: "Supzeol",
								age: 30,
								sex: 1,
								isguanzhu: false
							},
							{
								userpic: "../../static/demo/userpic/12.jpg",
								username: "Supzeol",
								age: 30,
								sex: 1,
								isguanzhu: false
							},
							{
								userpic: "../../static/demo/userpic/12.jpg",
								username: "Supzeol",
								age: 30,
								sex: 1,
								isguanzhu: false
							},
							{
								userpic: "../../static/demo/userpic/12.jpg",
								username: "Supzeol",
								age: 30,
								sex: 1,
								isguanzhu: false
							},
							{
								userpic: "../../static/demo/userpic/12.jpg",
								username: "Supzeol",
								age: 30,
								sex: 1,
								isguanzhu: false
							},
							{
								userpic: "../../static/demo/userpic/12.jpg",
								username: "Supzeol",
								age: 30,
								sex: 1,
								isguanzhu: false
							},
							{
								userpic: "../../static/demo/userpic/12.jpg",
								username: "Supzeol",
								age: 30,
								sex: 1,
								isguanzhu: false
							},
							{
								userpic: "../../static/demo/userpic/12.jpg",
								username: "Supzeol",
								age: 30,
								sex: 1,
								isguanzhu: false
							},
							{
								userpic: "../../static/demo/userpic/12.jpg",
								username: "Supzeol",
								age: 30,
								sex: 1,
								isguanzhu: false
							},
							{
								userpic: "../../static/demo/userpic/12.jpg",
								username: "Supzeol",
								age: 30,
								sex: 1,
								isguanzhu: false
							},
							{
								userpic: "../../static/demo/userpic/12.jpg",
								username: "Supzeol",
								age: 30,
								sex: 1,
								isguanzhu: false
							}
						]
					},
					{
						loadText: "上拉加载更多",
						list: [
							{
								userpic: "../../static/demo/userpic/12.jpg",
								username: "极尔文化",
								age: 20,
								sex: 0,
								isguanzhu: true
							},
							{
								userpic: "../../static/demo/userpic/12.jpg",
								username: "Supzeol",
								age: 30,
								sex: 1,
								isguanzhu: false
							},
							{
								userpic: "../../static/demo/userpic/12.jpg",
								username: "Supzeol",
								age: 30,
								sex: 1,
								isguanzhu: false
							},
							{
								userpic: "../../static/demo/userpic/12.jpg",
								username: "Supzeol",
								age: 30,
								sex: 1,
								isguanzhu: false
							},
							{
								userpic: "../../static/demo/userpic/12.jpg",
								username: "Supzeol",
								age: 30,
								sex: 1,
								isguanzhu: false
							},
							{
								userpic: "../../static/demo/userpic/12.jpg",
								username: "Supzeol",
								age: 30,
								sex: 1,
								isguanzhu: false
							},
							{
								userpic: "../../static/demo/userpic/12.jpg",
								username: "Supzeol",
								age: 30,
								sex: 1,
								isguanzhu: false
							},
							{
								userpic: "../../static/demo/userpic/12.jpg",
								username: "Supzeol",
								age: 30,
								sex: 1,
								isguanzhu: false
							},
							{
								userpic: "../../static/demo/userpic/12.jpg",
								username: "Supzeol",
								age: 30,
								sex: 1,
								isguanzhu: false
							},
							{
								userpic: "../../static/demo/userpic/12.jpg",
								username: "Supzeol",
								age: 30,
								sex: 1,
								isguanzhu: false
							},
							{
								userpic: "../../static/demo/userpic/12.jpg",
								username: "Supzeol",
								age: 30,
								sex: 1,
								isguanzhu: false
							}
						]
					},
					{
						loadText: "上拉加载更多",
						list: []
					},
				]
				
			}
		},
		// 监听导航按钮事件
		onNavigationBarButtonTap(e) {
			if (e.index==0) {
				uni.navigateBack({
					delta: 1
				});
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
						username: "Supzeol",
						age: 30,
						sex: 1,
						isguanzhu: false
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
		}
	}
</script>

<style>
/* 	.body {
		padding: 0 20rpx;
	} */
</style>
