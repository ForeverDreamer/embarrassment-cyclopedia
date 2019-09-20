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
		<view class="user-list u-f-ac">
			<image src="../../static/demo/userpic/12.jpg" mode="widthFix" lazy-load></image>
			<view>
				<view>极尔文化</view>
				<view style="display: inline-block;">
					<tag-sex-age age="20" sex="0"></tag-sex-age>
				</view>
			</view>
			<view class="icon iconfont icon-xuanze-yixuan u-f-ajc"></view>
		</view>
	</view>
</template>

<script>
	import swiperTabHead from "../../components/index/swiper-tab-head.vue"
	import tagSexAge from "../../components/common/tag-sex-age.vue"

	export default {
		components: {
			swiperTabHead,
			tagSexAge
		},
		data() {
			return {
				tabIndex: 0,
				tabBars: [
					{ name: "互关", id: "huguan", num: 10 },
					{ name: "关注", id: "guanzhu", num: 20 },
					{ name: "粉丝", id: "fensi", num: 30 },
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
		methods: {
			// tabbar点击事件
			tabtap(index) {
				this.tabIndex = index;
			}
		}
	}
</script>

<style>
	.body {
		border: 1rpx solid;
		padding: 0 20rpx;
	}
	.user-list {
		border: 1rpx solid green;
		padding: 20rpx 0;
		border-bottom: 1rpx solid #EEEEEE;
	}
	.user-list>image {
		width: 100rpx;
		height: 100rpx;
		border-radius: 100%;
		margin-right: 20rpx;
		flex-shrink: 0;
	}
	.user-list>view {
		border: 1rpx solid;
	}
	.user-list>view:first-of-type {
		flex: 1;
		border: 1rpx solid red;
	}
	.user-list>view:first-of-type>view:first-child {
		border: 1rpx solid yellow;
		font-size: 35rpx;
		font-weight: bold;
		padding-left: 10rpx;
	}
	.user-list>view:last-of-type {
		width: 80rpx;
		border: 1rpx solid blue;
		color: #CCCCCC;
	}
</style>
