<template>
	<view>
		<!-- 自定义导航栏 -->
		<news-nav-bar :tabBars="tabBars" :tabIndex="tabIndex" @change-tab="changeTab"></news-nav-bar>
		<view class="uni-tab-bar">
			<swiper class="swiper-box" 
			:style="{height:swiperHeight+'px'}" 
			:current="tabIndex" 
			@change="tabChange">
				<!-- 关注 -->
				<swiper-item>
					<scroll-view scroll-y class="list" @scrolltolower="loadMore">
						<block v-for="(item, index) in guanzhu.list" :key="index">
							<common-list :item="item" :index="index"></common-list>
						</block>
						<!-- 上拉加载 -->
						<loadMore :loadText="guanzhu.loadText"></loadMore>
					</scroll-view>
				</swiper-item>
				<!-- 话题 -->
				<swiper-item>
					<scroll-view scroll-y class="list">
						<!-- 搜索框 -->
						<view class="seach-input">
							<input class="uni-input" 
							placeholder-class="icon iconfont icon-sousuo topic-search" 
							placeholder="搜索内容" />
						</view>
						<!-- 轮播图 -->
						<swiper class="topic-swiper" :indicator-dots="true" 
						:autoplay="true" :interval="3000" :duration="1000">
							<block v-for="(item, index) in topic.swiper" :key="index">
								<swiper-item>
									<image :src="item.src" mode="widthFix" lazy-load></image>
								</swiper-item>
							</block>
						</swiper>
						<!-- 热门分类 -->
						<topic-nav :nav="topic.nav"></topic-nav>
						<!-- 最近更新 -->
						<view class="topic-new">
							<view>最近更新</view>
							<block v-for="(item, index) in topic.list" :key="index">
								<topic-list :item="item" :index="index"></topic-list>
							</block>
						</view>
					</scroll-view>
				</swiper-item>
			</swiper>
		</view>
	</view>
</template>

<script>
	import newsNavBar from "../../components/news/news-nav-bar.vue"
	import commonList from "../../components/common/common-list.vue"
	import loadMore from "../../components/common/load-more.vue"
	import topicNav from "../../components/news/topic-nav.vue"
	import topicList from "../../components/news/topic-list.vue"
	
	export default {
		components: {
			newsNavBar,
			commonList,
			loadMore,
			topicNav,
			topicList
		},
		data() {
			return {
				swiperHeight: 500,
				tabIndex: 0,
				tabBars: [
					{name: "关注", id: "guanzhu"},
					{name: "话题", id: "topic"}
				],
				guanzhu: {
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
				topic: {
					swiper: [
						{ src: "../../static/demo/banner1.jpg" },
						{ src: "../../static/demo/banner2.jpg" },
						{ src: "../../static/demo/banner3.jpg" }
					],
					nav: [
						{ name: "最新" },
						{ name: "游戏" },
						{ name: "打卡" },
						{ name: "情感" },
						{ name: "故事" },
						{ name: "喜爱" }
					],
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
						}
					]
				}
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
			// 点击切换
			changeTab(index) {
				this.tabIndex = index;
			},
			// 滑动事件
			tabChange(e) {
				this.tabIndex = e.detail.current;
			},
			// 上拉加载
			loadMore() {
				if (this.guanzhu.loadText != "上拉加载更多") {
					return;
				}
				// 修改状态
				this.guanzhu.loadText = "加载中...";
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
					this.guanzhu.list.push(obj);
					this.guanzhu.loadText = "上拉加载更多";
				}, 1000)
				// this.guanzhu.loadText = "没有更多数据了";
			},
		}
	}
</script>

<style>
	.seach-input {
		/* border: 1rpx solid; */
		padding: 20rpx;
	}
	.seach-input>input {
		/* border: 1rpx solid; */
		background: #F4F4F4;
		border-radius: 10rpx;
	}
	.topic-search {
		display: flex;
		justify-content: center;
		font-size: 27rpx;
	}
	.topic-swiper {
		padding: 0 20rpx 20rpx 20rpx;
	}
	.topic-swiper image {
		width: 100%;
		border-radius: 10rpx;
	}
	.topic-new {
		padding: 20rpx;
	}
	.topic-new>view:first-child {
		padding-bottom: 22rpx;
		font-size: 26rpx;
		font-weight: bold;
		color: #363636;
	}
</style>
