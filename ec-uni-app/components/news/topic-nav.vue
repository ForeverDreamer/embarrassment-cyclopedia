<template>
	<view class="topic-nav">
		<view class="u-f-ac u-f-jsb">
			<view>热门分类</view>
			<view class="u-f-ac" @tap="openTopicNav">
				更多<view class="icon iconfont icon-jinru"></view>
			</view>
		</view>
		<view class="u-f-ac u-f-jsb">
			<block v-for="(item, index) in nav" :key="index">
				<view>{{item.name}}</view>
			</block>
		</view>
	</view>
</template>

<script>
	export default {
		props: {
			nav: Array
		},
		methods: {
			openTopicNav() {
				uni.navigateTo({
					url: '../../pages/topic-nav/topic-nav',
				});
			}
		}
	}
</script>

<style scoped>
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
