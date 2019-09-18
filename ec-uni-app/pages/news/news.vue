<template>
	<view>
		<!-- 自定义导航栏 -->
		<uni-nav-bar status-bar="true" @click-right="openAdd" >
			<!-- 左边 -->
			<view slot="left" class="nav-left">
				<view class="icon iconfont icon-qiandao"></view>
			</view>
			<!-- 中间 -->
			<view class="nav-tab-bar u-f-ajc">
				<block v-for="(tab, index) in tabBars" :key="tab.id">
					<view class="u-f-ajc" :class="{'active': tabIndex==index}" @tap="changeTab(index)">
						{{tab.name}}
						<view v-if="tabIndex==index" class="nav-tab-bar-line"></view>
					</view>
				</block>
			</view>
			<!-- 右边 -->
			<view  slot="right" class="nav-right u-f-ajc">
				<view class="icon iconfont icon-bianji1"></view>
			</view>
		</uni-nav-bar>
		<!-- 列表 -->
		<view class="common-list u-f">
			<view class="common-list-1">
				<image src="../../static/demo/userpic/12.jpg" mode="widthFix" lazy-load></image>
			</view>
			<view class="common-list-r">
				<view class="u-f-ac u-f-jsb">
					<view class="u-f-ac">
						昵称
						<view class="tag-sex icon iconfont icon-nan">25</view>
					</view>
					<view class="icon iconfont icon-zengjia">关注</view>
				</view>
				<view>我是标题</view>
				<view class="u-f-ajc">
					<!-- 图片 -->
					<image src="../../static/demo/datapic/13.jpg" mode="widthFix" lazy-load></image>
					<!-- 视频 -->
					<view class="common-list-play icon iconfont icon-bofang"></view>
					<view class="common-list-playinfo">
						20w 次播放 2:47
					</view>
				</view>
				<view class="u-f-ac u-f-jsb">
					<view>深圳 龙岗</view>
					<view class="u-f-ac">
						<view class="icon iconfont icon-zhuanfa">10</view>
						<view class="icon iconfont icon-pinglun1">20</view>
						<view class="icon iconfont icon-dianzan1">30</view>
					</view>
				</view>
			</view>
		</view>
	</view>
</template>

<script>
	import uniNavBar from "../../components/uni-nav-bar/uni-nav-bar.vue"
	
	export default {
		components: {
			uniNavBar
		},
		data() {
			return {
				tabIndex: 0,
				tabBars: [
					{name: "关注", id: "guanzhu"},
					{name: "话题", id: "topic"}
				]
			}
		},
		methods: {
			changeTab(index) {
				this.tabIndex = index;
			},
			openAdd() {
				// 打开发布页面
				uni.navigateTo({
					url: '../add-input/add-input'
				});
			}
		}
	}
</script>

<style>
/* 	.nav-left, .nav-right {
		border: 1rpx solid;
	} */
	.nav-left>view, .nav-right>view {
		font-size: 40rpx;
	}
	.nav-left>view {
		color: #FF9619;
	}
	.nav-left {
		margin-left: 16rpx;
	}
	.nav-right {
		width: 100%;
	}
	.nav-tab-bar {
		width: 100%;
		margin-left: -30rpx;
		position: relative;
	}
	.nav-tab-bar>view {
/* 		border: 1rpx solid; */
		font-size: 32rpx;
		padding: 0 15rpx;
		font-weight: bold;
		color: #969696;
	}
	.active {
		color: #333333!important;
	}
	.nav-tab-bar-line {
		border-bottom: 5rpx solid #FEDE33;
		border-top: 5rpx solid #FEDE33;
		width: 70rpx;
		border-radius: 20rpx;
		position: absolute;
		bottom: 5rpx;
	}
	.common-list {
		padding: 20rpx;
	}
	.common-list-1 {
		flex-shrink: 0;
	}
	.common-list-1 image {
		width: 90rpx;
		height: 90rpx;
		border-radius: 100%;
	}
	.common-list-r {
		flex: 1;
		margin-left: 15rpx;
		border-bottom: 1rpx solid #EEEEEE;
		padding-bottom: 10rpx;
	}
	.common-list-r>view:nth-child(3)>image {
		width: 100%;
		border-radius: 10rpx;
	}
	.common-list-r>view:nth-child(1)>view:first-child {
		color: #999999;
		font-size: 30rpx;
	}
	.tag-sex {
		background: #44B3FF;
		color: #FFFFFF;
		font-size: 23rpx;
		padding: 5rpx 10rpx;
		margin-left: 10rpx;
		border-radius: 20rpx;
		line-height: 22rpx;
	}
	.common-list-r>view:nth-child(1)>view:last-child {
		background: #EEEEEE;
		padding: 0 10rpx;
		font-size: 26rpx;
	}
	.common-list-r>view:nth-child(2) {
		font-size: 32rpx;
		padding: 10rpx 0;
	}
	.common-list-r>view:nth-child(3) {
		position: relative;
	}
	.common-list-play, .common-list-playinfo {
		position: absolute;
		color: #FFFFFF;
	}
	.common-list-play {
		font-size: 130rpx;
	}
	.common-list-playinfo {
		right: 10rpx;
		bottom: 10rpx;
		background: rgba(51, 51, 51, 0.73);
		border-radius: 10rpx;
		padding: 0 20rpx;
		font-size: 26rpx;
	}
	.common-list-r>view:nth-child(4)>view {
		color: #AAAAAA;
	}
	.common-list-r>view:nth-child(4)>view:nth-child(2)>view {
		margin-left: 10rpx;
		padding-left: 5rpx;
		font-size: 28rpx;
	}
</style>
