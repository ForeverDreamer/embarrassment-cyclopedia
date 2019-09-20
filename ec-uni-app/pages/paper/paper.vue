<template>
	<view class="body">
		<!-- 小纸条列表 -->
		<view class="paper-list u-f-ac">
			<image src="../../static/demo/userpic/12.jpg" mode="widthFix" lazy-load style="border: 1rpx solid;"></image>
			<view>
				<view class="u-f-ac u-f-jsb">
					<view>JIA一勺</view>				
					<view>20:21</view>
				</view>
				<view class="u-f-ac u-f-jsb">
					<view>赵丽颖《知否》一句话打脸，“读书...</view>
					<uni-badge text="45" type="warning" />
				</view>
			</view>
		</view>
		
	</view>
</template>

<script>
	import uniBadge from '@/components/uni-badge/uni-badge.vue'

	export default {
		components: {
			uniBadge
		},
		data() {
			return {
				
			}
		},
		methods: {
			
		}
	}
</script>

<style>
	.body {
		border: 1rpx solid;
		padding: 0 20rpx;
	}
	.paper-list {
		border: 1rpx solid;
		border-bottom: 1rpx solid #EEEEEE;
		padding: 20rpx 0;
	}
	.paper-list>image {
		width: 100rpx;
		height: 100rpx;
		border-radius: 100%;
		margin-right: 20rpx;
		flex-shrink: 0;
	}
	.paper-list>view {
		border: 1rpx solid;
		flex: 1;
	}
	.paper-list>view>view:first-child {
		border: 1rpx solid;
		font-size: 35rpx;
	}
	.paper-list>view>view:first-child>view:first-child {
		border: 1rpx solid;
	}
	.paper-list>view>view:first-child>view:last-child {
		border: 1rpx solid;
		color: #CBCBCB;
	}
	.paper-list>view>view:last-child>view {
		border: 1rpx solid;
		color: #ADADAD;
		font-size: 28rpx;
	}
</style>
