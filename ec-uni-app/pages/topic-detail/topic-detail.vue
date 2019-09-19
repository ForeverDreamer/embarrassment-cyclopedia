<template>
	<view>
		<!-- 模糊背景 -->
		<view class="topic-bg">
			<image src="../../static/demo/topicpic/13.jpeg" mode="aspectFill" lazy-load></image>
		</view>
		<!-- 话题信息 -->
		<view class="topic-info">
			<view class="topic-info-t u-f-ac">
				<image src="../../static/demo/topicpic/13.jpeg" mode="widthFix" lazy-load></image>
				<view>#忆往事，敬余生#</view>
			</view>
			<view class="topic-info-c u-f-ac">
				<view>动态 100</view>
				<view>今日 100</view>
			</view>
			<view class="topic-info-b">
				面试官：在电梯里巧遇马云你会怎么做？90后女孩的回答当初被录用
			</view>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				
			}
		},
		methods: {
			
		}
	}
</script>

<style>
	.topic-bg {
		width: 100%;
		height: 300rpx;
		position: relative;
		overflow: hidden;
	}
	.topic-bg image {
		width: 100%;
		position: absolute;
		filter: blur(10px);
	}
	.topic-info {
		padding: 0 25rpx;
	}
	.topic-info-t {
		position: relative;
	}
	.topic-info-t>image{
		width: 150rpx;
		height: 150rpx;
		border-radius: 20rpx;
		position: absolute;
		top: -75rpx
	}
	.topic-info-t>view{
		font-size: 35rpx;
		margin-left: 165rpx;
		flex: 1;
	}
	.topic-info-c {
		padding: 35rpx 0 15rpx 0;
	}
	.topic-info-c>view {
		color: #CDCDCD;
	}
	.topic-info-b {
		color: #A3A3A3;
		font-size: 32rpx;
		padding-bottom: 10rpx;
	}
</style>
