<template>
	<view class="common-list u-f animated fadeIn fast">
		<view class="common-list-1">
			<image :src="item.userpic" mode="widthFix" lazy-load></image>
		</view>
		<view class="common-list-r">
			<view>
				<view class="u-f-ac u-f-jsb">
					<view class="u-f-ac">
						{{item.username}}
						<tag-sex-age :sex="item.sex" :age="item.age"></tag-sex-age>
					</view>
					<view v-show="!isguanzhu" @tap="guanzhu" class="icon iconfont icon-zengjia">
						关注
					</view>
				</view>
				<view class="common-list-r-time">26天前</view>
			</view>
			<view>{{item.title}}</view>
			<view class="u-f-ajc" style="flex-direction: column;">
				<!-- 图片 -->
				<block v-for="(pic, index) in item.morepic" :key="index">
					<image :src="pic" mode="widthFix" lazy-load @tap="imgdetail(index)" style="margin-bottom: 20rpx;">
					</image>
				</block>
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
			item: Object
		},
		data() {
			return {
				isguanzhu: this.item.isguanzhu
			}
		},
		methods: {
			imgdetail(index) {
				uni.previewImage({
					current: index,
					urls: this.item.morepic
				})
			},
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
	@import url("../../common/list.css");

	.common-list-r {
		border-bottom: 0;
	}

	.common-list {
		border-bottom: 1rpx solid #EEEEEE;
	}

	.common-list-r-time {
		padding: 0 !important;
		color: #CCCCCC !important;
		font-size: 15rpx;
		background: #FFFFFF !important;
	}

	.common-list-r>view:nth-child(1)>view:nth-child(1)>view:first-child {
		color: #999999;
		font-size: 30rpx;
	}

	.common-list-r>view:nth-child(1)>view:nth-child(1)>view:last-child {
		background: #EEEEEE;
		padding: 0 10rpx;
		font-size: 26rpx;
	}
</style>
