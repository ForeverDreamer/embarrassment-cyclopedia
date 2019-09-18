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
						<view class="topic-nav">
							<view class="u-f-ac u-f-jsb">
								<view>热门分类</view>
								<view class="u-f-ac">
									更多<view class="icon iconfont icon-jinru"></view>
								</view>
							</view>
							<view class="u-f-ac u-f-jsb">
								<view>最新</view>
								<view>游戏</view>
								<view>打卡</view>
								<view>情感</view>
								<view>故事</view>
								<view>喜爱</view>
							</view>
						</view>
						<!-- 最近更新 -->
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
	
	export default {
		components: {
			newsNavBar,
			commonList,
			loadMore
		},
		data() {
			return {
				swiperHeight: 500,
				tabIndex: 1,
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
	.topic-nav {
		border-top: 1rpx solid #EEEEEE;
		border-bottom: 1rpx solid #EEEEEE;
		padding: 20rpx;
	}
	
	.topic-nav>view:first-child {
		margin-bottom: 10rpx;
	}
	.topic-nav>view:first-child>view {
		color: #B2B2B2;
	}
	.topic-nav>view:first-child>view:first-child {
		color: #333333;
		font-size: 32rpx;
	}
	.topic-nav>view:last-child>view {
		background: #F7F7F7;
		color: #B2B2B2;
		border-radius: 10rpx;
		padding: 10rpx 25rpx;
	}
</style>
