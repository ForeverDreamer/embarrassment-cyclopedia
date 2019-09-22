<template>
	<view class="paper-list u-f-ac animated fadeInLeft fast" @tap="opendetail">
		<image :src="item.userpic" mode="widthFix" lazy-load></image>
		<view>
			<view class="u-f-ac u-f-jsb">
				<view>{{item.username}}</view>				
				<view>{{item.time}}</view>
			</view>
			<view class="u-f-ac u-f-jsb">
				<view>{{item.data}}</view>
				<template v-if="item.notenum > 0"></template>
				<uni-badge :text="item.notenum" type="warning" />
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
		props: {
			item: Object,
			index: Number
		},
		methods: {
			opendetail() {
				uni.navigateTo({
					url: '../../pages/user-chat/user-chat'
				});
			}
		}
	}
</script>

<style scoped>
	.paper-list {
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
		flex: 1;
	}
	.paper-list>view>view:first-child {
		font-size: 35rpx;
	}
	.paper-list>view>view:first-child>view:last-child {
		color: #CBCBCB;
	}
	.paper-list>view>view:last-child>view {
		color: #ADADAD;
		font-size: 28rpx;
	}
</style>
