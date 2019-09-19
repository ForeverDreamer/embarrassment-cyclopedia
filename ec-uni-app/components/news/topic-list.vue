<template>
	<view class="topic-list u-f animated fadeInLeft fast" @tap="opendetail">
		<image :src="item.titlepic" mode="widthFix" lazy-load></image>
		<view>
			<view>#{{item.title}}#</view>
			<view>{{item.desc}}</view>
			<view>动态 {{item.totalnum}} 今日 {{item.todaynum}}</view>
		</view>
	</view>
</template>

<script>
	export default {
		props: {
			item: Object,
			index: Number
		},
		methods: {
			opendetail() {
				uni.navigateTo({
					url: '../../pages/topic-detail/topic-detail'
				});
			}
		}
	}
</script>

<style scoped>
	.topic-list {
		padding: 10rpx 0;
		border-bottom: 1rpx solid #EEEEEE;
		padding-bottom: 30rpx;
	}

	.topic-list image {
		width: 175rpx;
		height: 175rpx;
		border-radius: 10rpx;
		margin-right: 30rpx;
	}

	.topic-list>view>view {
		color: #A4A4A4;
		font-size: 24rpx;
	}

	.topic-list>view>view:first-child {
		color: #333333;
		font-size: 32rpx;
	}
</style>
