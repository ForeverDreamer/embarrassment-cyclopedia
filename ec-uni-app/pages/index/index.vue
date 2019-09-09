<template>
	<view class="index-list">
		<view class="index-list1 u-f-ac u-f-jsb">
			<view class="u-f-ac">
				<image src="../../static/demo/userpic/12.jpg" mode="widthFix" lazy-load></image>
				昵称
			</view>
			<view class="u-f-ac">
				<view class="icon iconfont icon-zengjia">关注</view>
			</view>
		</view>
		<view class="index-list2">
			我是标题
		</view>
		<view class="index-list3 u-f-ajc">
			<!-- 图片 -->
			<image src="../../static/demo/datapic/11.jpg" mode="widthFix" lazy-load></image>
			<!-- 视频 -->
			<view class="icon iconfont icon-bofang index-list-play"></view>
			<view class="index-list-playinfo">20w次播放 2:47</view>
		</view>
		<view class="index-list4 u-f-ac u-f-jsb">
			<view class="u-f-ac">
				<view class="u-f-ac">
					<view class="icon iconfont icon-icon_xiaolian-mian"></view>
					570
				</view>
				<view class="u-f-ac">
					<view class="icon iconfont icon-kulian"></view>
					2
				</view>
			</view>
			<view class="u-f-ac">
				<view class="u-f-ac">
					<view class="icon iconfont icon-pinglun1"></view>
					21
				</view>
				<view class="u-f-ac">
					<view class="icon iconfont icon-zhuanfa"></view>
					14
				</view>
			</view>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				title: '仿糗事百科'
			}
		},
		onLoad() {

		},
		methods: {

		}
	}
</script>

<style>
	.index-list {
		padding: 20upx;
		border-bottom: 1upx solid;
	}
	.index-list1>view:first-child {
		color: #999999;
	}
	.index-list1>view:first-child image {
		width: 85upx;
		height: 85upx;
		border-radius: 100%;
		margin-right: 10upx;
	}
	.index-list1>view:last-child {
		background: #F4F4F4;
		border-radius: 5upx;
		padding: 0 10upx;
	}
	.index-list2 {
		padding-top: 15upx;
		font-size: 32upx;
	}
	.index-list3 {
		position: relative;
		padding-top: 15upx;
	}
	.index-list3>image {
		width: 100%;
		border-radius: 20upx;
	}
	.index-list4 {
		padding: 15upx 0;
	}
	.index-list4>view {
		color: #999999;
	}
	.index-list4>view>view>view, .index-list4>view>view:first-child {
		margin-right: 15upx;
	}
	.index-list-play {
		position: absolute;
		font-size: 140upx;
		color: #FFFFFF;
	}
	.index-list-playinfo {
		position: absolute;
		background: rgba(51, 51, 51, 0.72);
		color: #FFFFFF;
		bottom: 8upx;
		right: 40upx;
		border-radius: 40upx;
		font-size: 22upx;
		padding: 0 12upx;
	}
</style>
