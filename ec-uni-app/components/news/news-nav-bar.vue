<template>
	<view>
		<uni-nav-bar fixed="true" status-bar="true" :border="false" @click-right="openAdd">
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
			<view slot="right" class="nav-right u-f-ajc">
				<view class="icon iconfont icon-bianji1"></view>
			</view>
		</uni-nav-bar>
	</view>
</template>

<script>
	import uniNavBar from "../../components/uni-nav-bar/uni-nav-bar.vue"
		
	export default {
		components: {
			uniNavBar
		},
		props: {
			tabBars: Array,
			tabIndex: Number
		},
		methods: {
			changeTab(index) {
				this.$emit("change-tab", index);
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

<style scoped>
	/* 	.nav-left, .nav-right {
			border: 1rpx solid;
		} */
	.nav-left>view,
	.nav-right>view {
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
		color: #333333 !important;
	}

	.nav-tab-bar-line {
		border-bottom: 5rpx solid #FEDE33;
		border-top: 5rpx solid #FEDE33;
		width: 70rpx;
		border-radius: 20rpx;
		position: absolute;
		bottom: 5rpx;
	}
</style>
