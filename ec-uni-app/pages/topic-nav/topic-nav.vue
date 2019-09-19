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
							<!-- 话题列表 -->
							<view class="topic-view">
								<block v-for="(item, index1) in items.list" :key="index1">
									<topic-list :item="item" :index="index1"></topic-list>
								</block>
							</view>
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
	import noThing from "../../components/common/no-thing.vue"
	import loadMore from "../../components/common/load-more.vue"
	import topicList from "../../components/news/topic-list.vue"
	
	export default {
		components: {
			swiperTabHead,
			noThing,
			loadMore,
			topicList
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
								titlepic: "../../static/demo/topicpic/13.jpeg",
								title: "淘宝记录簿",
								desc: "120斤到85斤 我的反转人生",
								totalnum: 50,
								todaynum: 10
							},
							{
								titlepic: "../../static/demo/topicpic/13.jpeg",
								title: "淘宝记录簿",
								desc: "120斤到85斤 我的反转人生",
								totalnum: 50,
								todaynum: 10
							},
							{
								titlepic: "../../static/demo/topicpic/13.jpeg",
								title: "淘宝记录簿",
								desc: "120斤到85斤 我的反转人生",
								totalnum: 50,
								todaynum: 10
							},
							{
								titlepic: "../../static/demo/topicpic/13.jpeg",
								title: "淘宝记录簿",
								desc: "120斤到85斤 我的反转人生",
								totalnum: 50,
								todaynum: 10
							},
							{
								titlepic: "../../static/demo/topicpic/13.jpeg",
								title: "淘宝记录簿",
								desc: "120斤到85斤 我的反转人生",
								totalnum: 50,
								todaynum: 10
							},
							{
								titlepic: "../../static/demo/topicpic/13.jpeg",
								title: "淘宝记录簿",
								desc: "120斤到85斤 我的反转人生",
								totalnum: 50,
								todaynum: 10
							},
							{
								titlepic: "../../static/demo/topicpic/13.jpeg",
								title: "淘宝记录簿",
								desc: "120斤到85斤 我的反转人生",
								totalnum: 50,
								todaynum: 10
							},
							{
								titlepic: "../../static/demo/topicpic/13.jpeg",
								title: "淘宝记录簿",
								desc: "120斤到85斤 我的反转人生",
								totalnum: 50,
								todaynum: 10
							}
						]
					},
					{
						loadText: "上拉加载更多",
						list: []
					},
					{
						loadText: "上拉加载更多",
						list: [
							{
								titlepic: "../../static/demo/topicpic/13.jpeg",
								title: "淘宝记录簿",
								desc: "120斤到85斤 我的反转人生",
								totalnum: 50,
								todaynum: 10
							},
							{
								titlepic: "../../static/demo/topicpic/13.jpeg",
								title: "淘宝记录簿",
								desc: "120斤到85斤 我的反转人生",
								totalnum: 50,
								todaynum: 10
							},
							{
								titlepic: "../../static/demo/topicpic/13.jpeg",
								title: "淘宝记录簿",
								desc: "120斤到85斤 我的反转人生",
								totalnum: 50,
								todaynum: 10
							},
							{
								titlepic: "../../static/demo/topicpic/13.jpeg",
								title: "淘宝记录簿",
								desc: "120斤到85斤 我的反转人生",
								totalnum: 50,
								todaynum: 10
							},
							{
								titlepic: "../../static/demo/topicpic/13.jpeg",
								title: "淘宝记录簿",
								desc: "120斤到85斤 我的反转人生",
								totalnum: 50,
								todaynum: 10
							},
							{
								titlepic: "../../static/demo/topicpic/13.jpeg",
								title: "淘宝记录簿",
								desc: "120斤到85斤 我的反转人生",
								totalnum: 50,
								todaynum: 10
							},
							{
								titlepic: "../../static/demo/topicpic/13.jpeg",
								title: "淘宝记录簿",
								desc: "120斤到85斤 我的反转人生",
								totalnum: 50,
								todaynum: 10
							},
							{
								titlepic: "../../static/demo/topicpic/13.jpeg",
								title: "淘宝记录簿",
								desc: "120斤到85斤 我的反转人生",
								totalnum: 50,
								todaynum: 10
							}
						]
					},
					{
						loadText: "上拉加载更多",
						list: [
							{
								titlepic: "../../static/demo/topicpic/13.jpeg",
								title: "淘宝记录簿",
								desc: "120斤到85斤 我的反转人生",
								totalnum: 50,
								todaynum: 10
							},
							{
								titlepic: "../../static/demo/topicpic/13.jpeg",
								title: "淘宝记录簿",
								desc: "120斤到85斤 我的反转人生",
								totalnum: 50,
								todaynum: 10
							},
							{
								titlepic: "../../static/demo/topicpic/13.jpeg",
								title: "淘宝记录簿",
								desc: "120斤到85斤 我的反转人生",
								totalnum: 50,
								todaynum: 10
							},
							{
								titlepic: "../../static/demo/topicpic/13.jpeg",
								title: "淘宝记录簿",
								desc: "120斤到85斤 我的反转人生",
								totalnum: 50,
								todaynum: 10
							},
							{
								titlepic: "../../static/demo/topicpic/13.jpeg",
								title: "淘宝记录簿",
								desc: "120斤到85斤 我的反转人生",
								totalnum: 50,
								todaynum: 10
							},
							{
								titlepic: "../../static/demo/topicpic/13.jpeg",
								title: "淘宝记录簿",
								desc: "120斤到85斤 我的反转人生",
								totalnum: 50,
								todaynum: 10
							},
							{
								titlepic: "../../static/demo/topicpic/13.jpeg",
								title: "淘宝记录簿",
								desc: "120斤到85斤 我的反转人生",
								totalnum: 50,
								todaynum: 10
							},
							{
								titlepic: "../../static/demo/topicpic/13.jpeg",
								title: "淘宝记录簿",
								desc: "120斤到85斤 我的反转人生",
								totalnum: 50,
								todaynum: 10
							}
						]
					},
					{
						loadText: "上拉加载更多",
						list: []
					},
					{
						loadText: "上拉加载更多",
						list: []
					},
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
						titlepic: "../../static/demo/topicpic/13.jpeg",
						title: "淘宝记录簿",
						desc: "120斤到85斤 我的反转人生",
						totalnum: 50,
						todaynum: 10
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
	.topic-view {
		padding: 0 20rpx;
	}
</style>
