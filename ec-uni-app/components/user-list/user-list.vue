<template>
	<view class="user-list u-f-ac animated fadeInLeft fast">
		<image :src="item.userpic" mode="widthFix" lazy-load></image>
		<view>
			<view>{{item.username}}</view>
			<view style="display: inline-block;">
				<tag-sex-age :age="item.age" :sex="item.sex"></tag-sex-age>
			</view>
		</view>
		<view class="icon iconfont u-f-ajc" 
		:class="[item.isguanzhu?'icon-xuanze-yixuan':'icon-zengjia1']">
		</view>
	</view>
</template>

<script>
	import tagSexAge from "../../components/common/tag-sex-age.vue"
	
	export default {
		components: {
			tagSexAge
		},
		props: {
			item: Object,
			index: Number
		}
	}
</script>

<style scoped>
	.user-list {
		padding: 20rpx 0 20rpx 20rpx;
		border-bottom: 1rpx solid #EEEEEE;
	}
	.user-list>image {
		width: 100rpx;
		height: 100rpx;
		border-radius: 100%;
		margin-right: 20rpx;
		flex-shrink: 0;
	}
	.user-list>view:first-of-type {
		flex: 1;
	}
	.user-list>view:first-of-type>view:first-child {
		font-size: 35rpx;
		font-weight: bold;
		padding-left: 10rpx;
	}
	.user-list>view:last-of-type {
		width: 80rpx;
		color: #CCCCCC;
	}
	.icon-zengjia1 {
		color: #F8791B!important;
	}
</style>
