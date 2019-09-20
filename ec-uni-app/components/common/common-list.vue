<template>
	<view class="common-list u-f animated fadeInLeft fast">
		<view class="common-list-1">
			<image :src="item.userpic" mode="widthFix" lazy-load></image>
		</view>
		<view class="common-list-r">
			<view class="u-f-ac u-f-jsb">
				<view class="u-f-ac">
					{{item.username}}
					<tag-sex-age :sex="item.sex" :age="item.age"></tag-sex-age>
				</view>
				<view v-show="!isguanzhu" @tap="guanzhu" class="icon iconfont icon-zengjia">
					关注
				</view>
			</view>
			<view>{{item.title}}</view>
			<view class="u-f-ajc">
				<!-- 图片 -->
				<image v-if="item.titlepic" :src="item.titlepic" mode="widthFix" lazy-load></image>
				<!-- 视频 -->
				<template v-if="item.video">
					<view class="common-list-play icon iconfont icon-bofang"></view>
					<view class="common-list-playinfo">
						{{item.video.looknum}}w 次播放 {{item.video.long}}
					</view>
				</template>
				<!-- 分享 -->
				<view v-if="item.share" class="common-list-share u-f-ac">
					<image :src="item.share.titlepic" mode="widthFix" lazy-load></image>
					<view>{{item.share.title}}</view>
				</view>
			</view>
			<view class="u-f-ac u-f-jsb">
				<view>{{item.path}}</view>
				<view class="u-f-ac">
					<view class="icon iconfont icon-zhuanfa">{{item.sharenum}}</view>
					<view class="icon iconfont icon-pinglun1">{{item.commentnum}}</view>
					<view class="icon iconfont icon-dianzan1">{{item.goodnum}}</view>
				</view>
			</view>
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
		},
		data() {
			return {
				isguanzhu: this.item.isguanzhu
			}
		},
		methods: {
			guanzhu() {
				this.isguanzhu = true;
				uni.showToast({
					title: '关注成功'
				});
			}
		}
	}
</script>

<style scoped>
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
		margin-bottom: 10rpx;
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
	.common-list-share {
		background: #EEEEEE;
		width: 100%;
		padding: 10rpx;
		border-radius: 10rpx;
	}
	.common-list-share>image {
		width: 200rpx;
		height: 150rpx;
		margin-right: 10rpx;
	}
</style>
